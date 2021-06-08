#### QuerySet API

---

一旦创建数据模型后，Django自动给予一套数据库抽象API，允许你创建、检索、更新和删除对象。

##### 创建对象

一个模型类代表一张数据表，一个模型类实例代表数据表中一行记录。

创建实例对象的两种方式：

> * 先用关键字初始化对象，然后调用save()将其存入数据库。
> * 直接调用create()方法，创建对象并更新至数据库。

```python

# save(force_insert = False, force_update = False, using=DEFAULT_DB_ALIAS, update_fields=None);

# 调用方法时，会将对象保存至数据库。如果想自定义保存行为，可以重写这个方法。
# 在调用save()之前无法确定实例对象的自增主键是什么，因为自增id是数据库计算的，也不是Django计算的，除非明确指定；
# 如果实例对象的主键属性设置为True(除None空字符串以外的值)，那么django会执行UPDATE；
# 如果实例对象的主键属性没被设置，或者没有更新任何信息(例如主键设置了一个数据库中不存在的值)，那么Django会执行INSERT；
# 如果实例对象执行save()，那么数据库中这条数据的所有字段都会被更新一次，无论字段是否有变化；
# 可以指定update_fields参数，可以是一个列表，列表中是需要更新的字段名；此时数据库只会对指定字段进行更新；
# 可以通过指定force_insert, force_update参数，让数据强制进行INSERT或UPDATE操作。

person = Person(name='admin', age=18)
person.save()

person = Person()
person.name = 'admin'
person.age = 19
person.save()


# create(**kwargs)

# 创建对象并将其全部保存在一个步骤中的便捷方法

#指定关键字参数
School.objects.create(school_name='清华',city='beijing')

#传递字典参数
sh_info = {'school_name': '北大', 'city': 'beijing'}
School.objects.create(**sh_info)

```

##### 删除对象

```python

# delete(using=DEFAULT_DB_ALIAS, keep_parents=False);

# 立刻删除对象，并返回被删除的对象数量和一个包含了每个被删除对象类型的数量的字典。也可以批量删除对象，所有的QuerySet都有delete()方法，它会删除QuerySet中的所有成员。
# 当Django删除某个对象时，默认会模仿SQL约束ON DELETE CASCADE的行为——换而言之，某个对象被删除时，关联对象也会被删除；这种约束行为由ForeignKey的on_delete参数指定。

# 删除某一个对象
school1.delete()

# 删除QuerySet中的所有成员
School.objects.filter(city='beijing').delete()

# 删除School的所有对象
School.objects.all().delete()

```

##### 更新对象

```python

# update(** kwargs)；

# 对QuerySet中指定的字段执行SQL更新查询，并返回匹配的行数（如果某些行已具有新值，则可能不等于更新的行数）。
# 可以同时跟新多个字段；
# 方法立即应用，执行后就改变了数据库的数据；
# QuerySet更新的唯一限制是，只能更新模型主表中的列，不能更新相关联的模型中的列。

# 更新一个列
Student.objects.filter(pk=2).update(age=18)
# 更新QuerySet中的多个对象中的多个列
st_info = {'age': 18, 'score': 666}
Student.objects.filter(id__lt=3).update(**st_info)
# 更新与其他model相关联的列
sh = School.objects.get(pk=4)
Student.objects.filter(pk=3).update(school=sh)

```


##### 检索对象

QuerySet API

```python
# 要从数据库检索对象，就要通过模型类的Manager构建一个QuerySet；一个QuerySet代表来自数据库中对象的一个集合，可以根据给定参数缩小查询结果量。在SQL的层面上， QuerySet对应SELECT语句，而过滤器对应类似 WHERE 或 LIMIT 的限制子句。

# QuerySet是惰性的，创建 QuerySet 并不会引发任何数据库活动，Django只有在QuerySet被使用时才执行查询操作。

# Manager 是一种接口，它赋予了Django模型操作数据库的能力。Django应用中每个模型拥有至少一个 Manager，默认名称是objects。Managers只能通过模型类访问，而不是通过模型实例，目的是强制分离“表级”操作和“行级”操作。

#model类可以直接调用
all()：返回一个包含数据表中所有对象的QuerySet；
get(**kwargs)：返回一个满足给定查询参数的对象，没有则DoesNotExist；
filter(**kwargs)：返回一个新的QuerySet，包含的对象满足给定查询参数；
exclude(**kwargs)：返回一个新的QuerySet，包含的对象不满足给定查询参数；

#QuerySet可以调用
order_by(*fields)：根据指定字段进行排序
values(*fields, **表达式)：
distinct(*field)：去掉重复的行
reverse()：反转查询集元素的顺序；
count()：返回一个整数，表示与数据库匹配的QuerySet中的对象数；
first()：返回查询集匹配的第一个对象
last()：返回查询集中的最后一个对象
exists()：如果QuerySet包含任何结果返回True，不包含则为False；
union(*other_qs，all=False)：组合其他QS的结果；
difference(*other_qs)：保留调用QS中存在，其他QS不存在的元素；

School.objects.all()  #<QuerySet [<School: 清华大学>, <School: 北京大学>, <School: 山东大学>, <School: 复旦大学>]>
School.objects.get(school_name='北京大学')  #北京大学
School.objects.filter(city='beijing')  #<QuerySet [<School: 清华大学>, <School: 北京大学>]>
School.objects.exclude(city='beijing')  #<QuerySet [<School: 山东大学>, <School: 复旦大学>]>
School.objects.filter(pk=1).values()  #<QuerySet [{'id': 1, 'school_name': '清华大学', 'city': 'beijing', 'pass_line': 685}]>
School.objects.values('city').distinct()  #<QuerySet [{'city': 'beijing'}, {'city': 'shandong'}, {'city': 'shanghai'}]>
School.objects.order_by('pass_line')  # <QuerySet [<School: 山东大学>, <School: 复旦大学>, <School: 北京大学>, <School: 清华大学>]>
School.objects.order_by('pass_line').reverse()#<QuerySet [<School: 清华大学>, <School: 北京大学>,<School: 复旦大学>,<School: 山东大学>]>
School.objects.count()  #4
School.objects.filter(city='beijing').first()  #清华大学
School.objects.filter(city='beijing').last()  #北京大学
School.objects.filter(pass_line__gt=500).exists()  #True
School.objects.filter(pass_line__gt=700).exists()  #False

```

字段查询

字段查找是指定SQL WHERE子句的内容的方式。它们被指定为QuerySet方法的关键字参数；通过给定的限制条件查找出相对应子集。

```python

in：在给定的可迭代对象中
gt, gte, lt, lte：大于小于
range：给定对象范围内
isnull：是否为空
exact, iexact：完全符合
contains, icontains：包含匹配
startswith, istartswith：开头
endswith, iendswith：结尾
regex, iregex：正则表达式

Student.objects.filter(age__in=[18,19])  #<QuerySet [<Student: Jerry>, <Student: Lee>]>
Student.objects.filter(age__gt=20)  #<QuerySet [<Student: Ming>]>
Student.objects.filter(age__lt=20)  #<QuerySet [<Student: Jerry>, <Student: Lee>]>
Student.objects.filter(score__range=[650, 700])  #<QuerySet [<Student: Jerry>]>
Student.objects.filter(age__isnull=True)  #<QuerySet []>
Student.objects.filter(student_name__exact='Ming')  #<QuerySet [<Student: Ming>]>
Student.objects.filter(student_name__contains='e')  #<QuerySet [<Student: Jerry>, <Student: Lee>]>
Student.objects.filter(student_name__startswith='L')  #<QuerySet [<Student: Lee>]>
Student.objects.filter(student_name__endswith='y')  #<QuerySet [<Student: Jerry>]>
Student.objects.filter(student_name__regex='[A-Z]e[a-z]*')  #<QuerySet [<Student: Jerry>, <Student: Lee>]>

```

聚合查询

```python
# Aggregate(*expressions, output_field = None, distinct = False, filter = None, ** extra)

# 聚合表达式是Func()表达式的一种特殊情况，查询需要一个聚合函数。

Avg()：返回给定表达式的平均值
Count()：返回给定表达式的总计数
Max()：返回给定表达式的最大值
Min()：返回给定表达式的最小值
Sum()：计算给定表达式的所有值的总和

from django.db.models import Avg, Count, Max, Min, Sum

Student.objects.aggregate(Avg('score'))  #{'score__avg': 618.0}
Student.objects.aggregate(Count('score'))  #{'score__count': 3}
Student.objects.count()  #3
Student.objects.aggregate(Max('score'))  #{'score__max': 666}
Student.objects.aggregate(min_value=Min('score'))  #{'min_value': 560}
Student.objects.aggregate(sums=Sum('score'))  #{'sums': 1854}

````

分组查询

```python
# annotate(*args, **kwargs)；

# 如果先使用values()方法对整体分组，聚合函数只能针对某组对象进行处理；而annotate()可以针对每组进行处理。

# 例如：查询每个城市的学校数量，和每个城市学校最高录取分数

School.objects.values('city').annotate(Count('pass_line'))
#<QuerySet [{'city': 'beijing', 'pass_line__count': 2}, {'city': 'shandong', 'pass_line__count': 1}, {'city': 'shanghai', 'pass_line__count': 1}]>
School.objects.values('city').annotate(Max('pass_line'))
#<QuerySet [{'city': 'beijing', 'pass_line__max': 685}, {'city': 'shandong', 'pass_line__max': 657}, {'city': 'shanghai', 'pass_line__max': 665}]>

```

F查询

```python
# 一个F()对象表示一个模型字段或注释的列的值。它可以引用模型字段值并使用它们执行数据库操作，而无需将它们从数据库中拉出到Python内存中。

# 让数据库而不是Python来做工作；

# 避免多线程中对数据库中字段的抢占；

# 减少一些操作所需的查询数量。

from django.db.models import F

school = School.objects.get(pk=3)
school.pass_line = F('pass_line') + 20
school.save()

school = School.objects.filter(pk=3)
school.update(F('pass_line') + 20)


# django遇到F()示例时，它会覆盖python运算符来创建一个封装的SQL表达式，指示数据库增加由school.pass_line表示的数据库字段。

# 无论school.pass_line的值是什么，python都不会知道，它完全由数据库处理，此时的F()实例就像一个数据库字段的引用。

# 使用F()函数保存值后,再次使用实例调用并不能拿到新的值.这是因为F()函数是数据库操作,并不是在内存中python进行的；要访问保存后的新值时，必须重新加载该对象。


school = School.objects.get(pk=school.pk)
# or
school.refresh_from_db()
# 保存F()实例后，赋值给模型字段的对象将会保留，每次执行save()时，字段的F()也会执行一次。


school = School.objects.get(pk=3)
school.pass_line = F('pass_line') + 20
school.save()
school.save()
# 如果pass_line初始值是500，最终值是540；通过在保存模型对象后重新加载模型对象，例如使用refresh_from_db()可以避免此持久性。

```


Q查询

```python
# 封装一组字段查询操作。

# 在字段查询中，可以使用,分割并列的查询条件；但字段中不能进行其他关系条件的查询。

# 使用Q()实例字段查询后，可以进行&|~等条件的查询。

from django.db.models import F

School.objects.filter(city='beijing', pass_line__gt=680)  #<QuerySet [<School: 清华大学>]>
School.objects.filter(Q(city='beijing') & Q(pass_line__gt=680)) #<QuerySet [<School: 清华大学>]>
School.objects.filter(Q(city='beijing') | Q(pass_line__gt=680)) #<QuerySet [<School: 清华大学>, <School: 北京大学>]>
School.objects.filter(~Q(city='beijing'))  #<QuerySet [<School: 山东大学>, <School: 复旦大学>]>
School.objects.filter(Q(pass_line__lt=660) & (Q(city='shandong') | Q(city='shanghai')))  #<QuerySet [<School: 山东大学>]>

# Q查询与字段查询共同使用时，字段查询需要放在Q()的后面。

School.objects.filter(Q(city='shandong') | Q(city='shanghai'), pass_line__lt=660)  #<QuerySet [<School: 山东大学>]>

con = Q()

q1 = Q()
q1.connector = 'OR'
q1.children.append(('id', 1))
q1.children.append(('id_lt', 2))
q1.children.append(('name_contains', 'hi'))

q2 = Q()
q2.connector = 'OR'
q2.children.append(('status', '在线'))

con.add(q1, 'AND')
con.add(q2, 'AND')

models.Tb1.objects.filter(con)
```

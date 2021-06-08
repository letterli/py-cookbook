#### 关联对象

---

模型中定义关联关系（ForeignKey, OneToOneField, ManyToManyField），该模型实例将会自动获取一套API，能快捷访问关联对象。

##### 一对一
OneToOneField(to, on_delete, parent_link=False, options)

 一对一的关系。

```python
#一个学生只能有一个学号和档案号
#一个学号和档案号只能属于一个学生
#身份信息和学生就可以建立一对一关联

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
    identify = models.OneToOneField('Identify', on_delete=models.CASCADE)

class Identify(models.Model):
    student_number = models.IntegerField()
    archive_number = models.IntegerField()

# 一对一查找

# 正向查找
s = Student.objects.get(pk=2)
print(s.identify)

# 反向查找
id = Identify.objects.get(pk=1)
print(s.student)


```

##### 一对多

ForeignKey(to, on_delete, options)

一对多的关系。需要两个位置参数：与模型相关的类和on_delete选项。在数据库上自动创建数据库索引ForeignKey，您可以通过设置db_index为禁用此功能False。
可以通过'self'来创建递归关系，与自身具有一对多的关系。
当添加一个外键后，Django追加_id字段名来创建数据库的列名；Student的数据表中的school字段将变为school_id列。

```python

# 表结构

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=17)
    school = models.ForeignKey('School', on_delete=models.CASCADE)


class School(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=100)


# 创建对象
# 在创建实例对象时，关联字段显式指定一个关联对象，或者关联字段id指定一个对象id；

#通过字段属性指定关联的对象
sh_obj1 = School.objects.filter(city='上海').first()
student1_info = {
    'student_name': '小海',
    'age': 21,
    'score': 662,
    'school': sh_obj1
}
Student.objects.create(**student1_info)

#通过指定表列名指定关联对象的id值，也可以是个数字
sh_obj2 = School.objects.filter(pass_line__lt=660).order_by('pass_line').last()
student2_info = {
    'student_name': '大B',
    'age': 20,
    'score': 672,
    'school_id': sh_obj2.id
}
Student.objects.create(**student2_info)

# 通过关联对象反向创建一个对象实例。

sh = School.objects.get(pk=1)
sh.student_set.create(
    student_name='大黄',
    age=23,
    score=581,
)

# 正向查找
# 通过双下划线直接调用关联对象中的字段。

obj = Student.objects.filter(school__city='上海')
print(obj)  #<QuerySet [<Student: 小海>]>

#连表查询，查询每个城市的学生人数
obj = Student.objects.values('school__city').annotate(Count('age'))
print(obj)  #<QuerySet [{'school__city': '上海', 'age__count': 1}, {'school__city': '济南', 'age__count': 2}]>


# 模型的实例能通过其属性方便的访问关联（外部的）对象
#通过属性调用关联对象
student = Student.objects.filter(student_name='小海').first()
print(student.school)  #上海交通大学

#可以对外键进行修改，通过save()保存至数据库
obj = School.objects.filter(city='济南').first()
student.school = obj
student.save()
student.refresh_from_db()
print(student.school)  #山东大学

# 如果ForeignKey字段配置了null=True，可以指定值为 None 移除关联
student.school = None
student.save()
student.refresh_from_db()
print(student.school)  # None


# 反向查找
# 反向查找，可以通过外键类名的小写，加上_set，返回一个QuerySet。
sh_obj = School.objects.filter(city='济南').last()
st_obj = sh_obj.student_set.all()
print(st_obj)  #<QuerySet [<Student: 阿拉蕾>, <Student: 大B>]>
#返回的QuerySet也可以调用筛选、排序等API
obj = st_obj.order_by('age')
print(obj)  #<QuerySet [<Student: 大B>, <Student: 阿拉蕾>]>


# 模型的实例能通过其属性方便的访问关联（外部的）对象。
# 查找哪些学校中有年龄小于18的学生
obj = School.objects.filter(student__age__lt=18)
print(obj)  #<QuerySet [<School: 北京大学>]>


# add(*objs, bulk = True, through_defaults = None)
# 将指定的模型对象添加到相关的对象集。

st = Student.objects.get(student_name='小海')
print(st.school)  #上海交通大学
sh = School.objects.get(pk=4)
sh.student_set.add(st)
print(st.school)  #复旦大学

# 在ForeignKey关系的情况下，使用QuerySet.update()更新至数据库，也可以使用bulk=False参数调用QuerySet.save()
# add()也接受关联指向的字段作为参数，可以改写为sh.student_set.add(4)


# remove(*objs, bulk=True)
# 从相关对象集中删除指定的模型对象；


st = Student.objects.get(student_name='小海')
print(st.school)  # 复旦大学
sh = School.objects.get(school_name='复旦大学')
sh.student_set.remove(st)
st.refresh_from_db()  #重新获取实例对象
print(st.school)  #None

# 在ForeignKey关系的情况下，此方法仅在null=True情况下存在；
# 默认使用QuerySet.update()更新至数据库，也可以使用bulk=False参数调用QuerySet.save()
# remove()也接受关联指向的字段作为参数，可以改写为sh.student_set.remove(4)


# clear(bulk=True)
# 从相关对象集中删除所有对象；


sh = School.objects.get(school_name='复旦大学')
sh.student_set.clear()

# 这不会删除相关对象，只是将关联关系取消。

# 只在ForeignKeys字段null=True时才可以用，它也接受bulk关键字参数。



# set(objs, bulk=True, clear=False, through_defaults=None)
# 替换相关对象集;


new_list = [obj1, obj2, obj3]
obj.related_set.set(new_list)

#如果clear为False(默认)，将利用remove()删除新集中缺少的元素，并且仅添加新元素；如果clear=True，则调用clear()方法，并立即添加整个集合。

#对于ForeignKey对象，bulk 参数传递给add()和remove()的。

#由于set()是复合操作，因此受竞争条件的限制。

```

##### 多对多

ManyToManyField(to, options)
多对多的关系。需要一个位置参数：与模型相关的类。

```python
# Django创建了一个中间数据表来建立多对多关系，默认情况下，此表名称是使用多对多字段的名称以及包含它的模型的表名生成的。
# 对于多对多关联关系的两个模型，可以在任何一个模型中添加ManyToManyField字段，但只能选择一个模型设置该字段，不能同时在两模型中添加该字段。

#一个学生可以有多个任课老师，
#一个老师也可以教多个学生，
#学生和老师就可以建立多对多关联

class Student(models.Model):
    student_name = models.CharField(max_length=20)
    age = models.IntegerField(default=15)
    teachers = models.ManyToManyField('Teacher')

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20)
    sex = models.BooleanField(default=True)


# 在指定ManyToManyField字段时，通过through参数可以指定自定义的关系表，也就可以自定义关系表的表结构；
class Student(models.Model):
    student_name = models.CharField(max_length=20)
    age = models.IntegerField(default=15)
    score = models.IntegerField(default=560)
    teacher = models.ManyToManyField('Teacher', through="StudentToTeacher")

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20)
    sex = models.BooleanField(default=True)
    course = models.CharField(max_length=20, default='语文')

class StudentToTeacher(models.Model):
    st_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)

    class Meta:
        unique_together = [
            ('student_id', 'student_id')  #两个字段联合唯一
        ]

# 在中间的关系表中，可以利用两个ForeignKey字段，分别指向两个关联对象，让他们在这张表中同时建立外键关系。

class Student(models.Model):
    student_name = models.CharField(max_length=20)
    age = models.IntegerField(default=15)
    score = models.IntegerField(default=560)

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20)
    sex = models.BooleanField(default=True)
    course = models.CharField(max_length=20, default='语文')

class StudentToTeacher(models.Model):
    st_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)

# 创建对象

# 多对多不可以在创建时直接指定关联对象；要先创建对象，然后再添加关联关系。

teacher_info = {
    'teacher_name': '鲁迅',
    'sex': False,
    'course': '语文'
}
Teacher.objects.create(**teacher_info)

student_info = {
    'student_name': '老王头',
    'age': 25,
    'score': 562,
}
Student.objects.create(**student_info)

# add(*objs, through_defaults = None)
# 将指定的模型对象添加到相关的对象集。
# 多对多关系不会调用save()方法（bulk参数不存在），而是使用QuerySet.bulk_create()创建关系。
# ManyToManyFeild()定义Student类中，那么通过Student对象添加Teacher对象，就被视为正向添加；反之为反向添加。反向调用时通过外键class名的小写，加上_set。


#正向添加
th = Teacher.objects.filter(course='语文').first()
st = Student.objects.filter(student_name='老王头').first()
st.teacher.add(th)
print(st.teacher.all())  #<QuerySet [<Teacher: 鲁迅>]>

#反向添加
th = Teacher.objects.get(pk=1)
st = Student.objects.filter(pk__lt=3)
th.student_set.add(*st)
print(th.student_set.all())  #<QuerySet [<Student: Jerry>, <Student: Ming>]>

# remove(*objs)
# 从相关对象集中删除指定的模型对象；

# clear()
# 从相关对象集中删除所有对象；

# set(objs, clear=False, through_defaults=None)
# 替换相关对象集;

# 多对多关联中的add()，set()和remove()放法能接收主键值，bulk关键字参数不存在。

```

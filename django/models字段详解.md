#### Django Model

---

##### Model简介

Django Model是一个ORM框架。模型准确且唯一的描述数据。model包含存储的数据的重要字段和行为。
每一个模型对应一张数据库表。

> * 每个模型都是一个python类，这些类继承django.db.models.Model;
> * 模型类每一个属性都相当于一个数据表的字段；
> * Django提供一个自动生成访问数据库的API;

##### 使用模型

定义模型时，每个字段都被定为一个类属性，并且每个属性映射为数据表列。
创建数据库时，会自动添加主键id字段。

```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(blank=False)

```

如果想使用自定义模型，需修改设置文件中的INSTALLED_APPS，设置中添加包含models.py文件的模块名称。

```python
INSTALLED_APPS = [
    # ....
    'application.apps.UserConfig',
    # ....
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_passwd',
        'HOST': 'db_host',
        'PORT': db_port
    }
}

```

```shell
# 生成迁移文件
python manage.py makemigrations

# 执行数据库迁移
python manage.py migrate

```

##### models字段

```python
# 自增列
models.AutoField

# 字符串字段
models.CharField

# 布尔类型
models.BooleanField

# 用逗号分割的数字 = varchar
models.ComaSeparatedIntegerField

# 日期类型 date
models.DateField

# 日期类型 datetime
models.DateTimeField

# 十进制小数类型 = decimal
models.DecimalField

# 字符串类型（正则表达式邮箱） = varchar
models.EmailField

# 浮点类型 = double
models.FloatField

# 短整形
models.SmallIntegerField

# 整形
models.IntegerField

# 长整形
models.BigIntegerField

# 字符串类型（ip4正则表达式）
models.IPAddressField

# 字符串类型（ip4和ip6是可选的）
models.GenericIPAddressField

# 字符串 = longtext
models.TextField

# 时间
models.TimeField

# 字符串(地址正则表达式)
models.URLField

# 二进制
models.BinaryField

# 图片  在数据库中保存的是文件的路径
models.ImageField

# 文件
models.FileField

```

##### 字段参数

```python

# 数据库中字段是否可以为空,字段为空时，设置为NULL 默认:False
null=True

# django的 Admin 中添加数据时是否可允许空值 默认:False
blank=True

# 主键，对AutoField设置主键后，就会代替原来的自增 id 列
primary_key = False
　　
#　auto_now   自动创建---无论添加或修改，都是当前操作的时间
#　auto_now_add  自动创建---永远是创建时的时间

auto_now and auto_now_add

# choices
GENDER_CHOICE = (
    ('M', 'Male'),
    ('F', 'Female'),
)
gender = models.CharField(max_length=2, choices=GENDER_CHOICE)

# 字符串长度
max_length

# 默认值
default

# Admin中字段的显示名称
verbose_name　　

# 数据库中的字段名称 默认:属性名
name or db_column

# 不允许重复
unique=True　

# 数据库索引　默认:False
db_index=True　
　
# 在Admin里是否可编辑
editable=True

# 错误提示
error_messages=None

# 自动创建　
auto_created=False　

# 在Admin中提示帮助信息
help_text　

validators=[]

# 上传路径
upload-to

on_delete=model.CASCADE
#ForeignKey.on_delete：当ForeignKey删除引用的对象时，Django将模拟on_delete参数指定的SQL约束的行为 。

#    CASCADE, 删除引用的对象时，也删除引用它的对象；
#    PROTECT, 通过抛出异常来禁止删除引用的对象。
#    SET_NULL, 将引用设置为NULL，只有在null为True的情况下。
#    SET_DEFAULT, 设置默认值，ForeignKey必须设置默认值。
#    SET(...), 设置给定值。
#    DO_NOTHING, 不采取行动。如果数据库后端强制引用完整性，这将导致完整性错误，除非手动向数据库字段添加SQL on delete约束。

```

##### meta

使用内部的Meta类给model定义元数据。

```python

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(blank=False)

    class Meta:
        db_table = 'db_table_name'
        ordering = ['-created_at']
        get_latest_by = 'created_at'


# abstract
# 如果abstract=True，那么model为抽象基类；

# app_label
# 在其他地方写了一个模型类，而这个模型类是属于myapp的，那么需要指定app_label='myapp'；

# db_table
# 用于指定自定义数据库表名的；

# get_latest_by
# 由于Django的管理方法中有个lastest()方法，就是得到最近一行记录。如果你的数据模型中有 DateField 或 DateTimeField 类型的字段，你可以通过这个选项来指定lastest()是按照哪个字段进行选取的。

# managed
# 由于Django会自动根据模型类生成映射的数据库表，如果你不希望Django这么做，可以把managed的值设置为False。

# ordering
# 这个字段是告诉Django模型对象返回的记录结果集是按照哪个字段排序的。加负号为反序ordering = ['-create_time']

# permissions
# 创建此对象时进入权限表的额外权限。
# 指定了一个附加权限: can_deliver_pizzas
# permissions = (("can_deliver_pizzas", "Can deliver pizzas"),)
# 这是一个2-元素 tuple 的tuple或列表, 其中两2-元素 tuple 的格式为:(permission_code, human_readable_permission_name)。

# unique_together
# 一起使用的字段名称集必须是唯一的，这是一个列表，这些列表在一起考虑时必须是唯一的
# unique_together = [['driver', 'restaurant']]

# verbose_name
# 给model类起一个更可读的名字：

# verbose_name_plural
# model的复数名称
```



## 第六章：Django站点管理

---

### django.contrib 包
Django 自动管理工具是django.contrib的一部分。django.contrib是一套庞大的功能集,它是Django基本代码的组成部分。
Django框架就是由众多包含附加组件的基本代码构成。


django.contrib.admin 管理工具
django.contrib.auth 用户鉴别系统
django.contrib.sessions 支持匿名会话
django.contrib.comments  用户评注系统


### 激活管理界面

1.将 django.contrib.admin 加入setting.py的INSTALLED_APPS配置中。

2.保证INSTALLED_APPS中包含 django.contrib.auth, django.contrib.contenttypes and django.contrib.sessions 3个管理包。

3.确保MIDDLEWARE_CLASSES包含 django.middleware.common.CommonMiddleware,django.contrib.sessions.middleware.SessionMiddleware and django.contrib.auth.middleware.AuthenticationMiddleware

```python

    python manage.py makemigrations    # 创建admin迁移文件

    python manage.py migrate           # 迁移

    python manage.py createsuperuser   # 创建管理员账号

    # urls.py

    from django.contrib import admin

    urlpatterns = patterns('',
        (r'^admin/$', include(admin.site.urls))
    )

```

### 将app Models加入Admin管理中

app目录下admin.py，注册模块。

```python
    from django.contrib import admin
    from mysite.books.models import Publisher, Author, Book

    admin.site.register(Publisher)
    admin.site.register(Author)
    admin.site.register(Book)
```

### Admin如何工作

Django从urls.py引导URLconf,然后执行admin.autodiscover()语句。该函数遍历INSTALLED_APPS配置，寻找相关admin.py文件。
如果在指定的app目录下找到admin.py，它就执行其中的代码。

app应用程序目录下的admin.py，每次调用admin.site.register()都将那个模块注册到管理工具。管理工具只为那些明确注册了的模块显示一个编辑/修改界面。

应用程序 django.contrib.auth包含自身的admin.py，所以Users和Groups能在管理工具中自动显示。

综上所述，管理工具是Django应用程序，包含自己的模块、模板、视图和URLpatterns。 管理工具目录django/contrib/admin。


### 设置字段可选

所有字段默认blank=False，使得他们不允许输入空值。

```python
    class Author(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=40)
        email = models.EmailField(blank=True)
```

### 设置日期型和数字型字段可选

SQL中，日期型、时间型和数字型字段不接受空字符串。NULL的值不同于空字符串，null=True指定一个字段允许为NULL。

```python
    class Book(models.Model):
        title = models.CharField(max_length=40)
        authors = models.ManyToMany(Author)
        publisher = models.ForignKey(Publisher)
        publication_date = models.DateField(blank=True, null=True)
```

### 自定义字段标签

在模块中指定verbose_name自定义一个标签。

```python
    class Author(models.Model):
        email = models.EmailField(blank=True, verbose_name = 'e-mail')
```

### 自定义ModelAdmin类

Django 提供了大量针对特别模块自定义管理工具，这些选项都在ModelAdmin class里面。

AuthorAdmin 是从django.contrib.admin.ModelAdmin派生出来的子类，保存着一个类自定义配置。

```python
    from django.contrib import admin
    from models import Publisher, Author, Book

    class AuthorAdmin(admin.ModelAdmin):
        list_display = ('first_name', 'last_name', 'email')
        search_fields = ('first_name', 'last_name')

    class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'publisher', 'publication_date')
        # 日期排序
        list_filter = ('publication_date',)
        date_hierarchy = 'publication_date'
        # 排序
        ordering = ('-publication_date', )
        # 自定编辑表单
        fields = ('title', 'publisher', 'authors')
        # 多对多字段 展现成多选框
        filter_horizontal = ('authors', )


    admin.site.register(Publisher)
    admin.site.register(Author, AuthorAdmin)
    admin.site.register(Book, BookAdmin)
```

### 用户、用户组和权限

管理界面中每种可编辑的对象都有三种权限：创建许可、编辑许可和删除许可。

用户权限定义在模块级别，而不是对象级别上。

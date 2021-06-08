## 第一章：介绍Django

---

### 简介
Django是一个开放源代码的Web应用框架，由Python写成。
采用MVC的软件设计模式。模型M，视图V和控制器C. （更严格意义上来讲，应该属于MVP模式）
Django使得开发复杂的，数据库驱动的网站变得简单。


### MVC设计模式
MVC 是一种软件开发的方法，把代码的定义和数据访问的方法（模型）与请求逻辑（控制器）还有
用户接口（视图）分开。

```python
    # models.py   (database table)

    from django.db import models

    class Book(models.Model):
        name = models.CharField(max_length=50)
        pub_date = models.DateField()


    # views.py (business logic)

    from django.shortcuts import render_to_response
    from models import Book

    def latestBooks(request):
        bookLists = Book.objects.order_by('-pub_date')[:10]
        return render_to_response('latest_books.html', {'bookLists' : bookLists})

    # urls.py  (URL configuration)

    from django.conf.urls.defaults import *
    import views

    urlpatterns = patterns('',
        (r'^latest/$', views.latestBooks),
    )

    # latest_books.html  (template)

    <html>
    <head>
        <title><Books></title>
    </head>
    <body>
        <h1>Books</h1>
        <ul>
            {% from book in bookLists %}
            <li>{{ book.name }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
```

1. models.py 文件主要用一个Python类来描述数据表，称为模型(model)。用来创建、检索、更新、删除数据库记录。

2. views.py 页面的业务逻辑。latestBooks 函数称为视图函数。

3. urls.py 路由URL调用视图函数。 /latest/ URL将会调用latestBooks() 视图函数

4. latest_books.html html模板。


### Django 历史

Django由 Kansas州 Lawrence城中的一个网络开发小组编写的。它诞生于2003年秋天，那时Lawrence Journal-World
报纸的程序员Adrian Holovaty和Simon Willison开始用Python 来编写程序。

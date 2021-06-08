## 第三章：视图和URL配置

---

### 视图 (控制器)

创建views.py视图文件。首先导入django.http模块导入HttpResponse类。
创建hello视图函数。每个视图函数至少要有一个参数，通常名叫request。request是一个触发视图、包含
当前web请求信息的对象，是类django.http.HttpRequest的一个实例。

```python
    from django.http import HttpResponse

    def hello(request):
        return HttpResponse('Hello World.')
```

一个视图函数就是Python的一个函数。这个函数第一个参数的类型是HttpRequest,返回HttpResponse实例。

### URLconf (路由)

URLconf本质是URL模式以及要求为该URL模式调用的视图函数之间的映射。

```python
    from mysite.views import hello

    urlpatterns = patterns('',
        url(r'^$', hello)
    )
```

如果喜欢URL都以'/'结尾，需要URL后添加斜杠，并设置APPEND_SLASH = True
如果不喜欢URL以'/'结尾，根据自己的意愿来添加尾斜杠，设置APPEND_SLASH = False


### Django处理请求

所有始于setting文件。当你运行python manage.py runserver，脚本将在于manage.py同一个目录下查找名为
setting.py的文件。setting.py文件包含Django项目的配置信息，包括TEMPLATE_DIRS,DATABASE_NAME等，最
重要的设置是ROOT_URLCONF，它将作为URLconf告诉Django在这个站点中那些Python的模块将被用到。

ROOT_URLCONF = 'mysite.urls'


总结如下：
1. 进来的请求转入/hello/。

2.Django通过在ROOT_URLCONF配置来决定根URLconf。

3.Django在URLconf中的所有URL模式中，查找第一个匹配/hello/的条目。

4.如果查找到匹配,将调用相应的视图函数。

5.视图函数返回一个HttpResponse.

6.Django转换HttpResponse为一个合适的HTTP response,以 Web page 显示出来。


### 正则表达式

| 符号        | 匹配   |
| --------   | -----:  |
| .     | 任意单一字符 |
| \d        |   任意一位数字   |
| [A-Z]        |    A到Z中任意一个字符（大写）    |
| [a-z]     | a到z中任意一个字符（小写） |
| [A-Za-z]        |   a-z中任意一个字符（不区分大小写）   |
| +        |    匹配一个或更多    |
| [^/]+     | 一个或多个不为'/'的字符 |
| ?        |   零个或一个之前的表达式   |
| *        |    匹配零个或多个    |
| {1, 3}     | 介于一个和三个之间的表达式 (\d{1, 3} 匹配一个或两个三个数字) |


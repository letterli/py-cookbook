## 第八章：高级视图和URL配置

---

### URLconf技巧

流线型化函数导入

```python
    from django.conf import settings
    from django.conf.urls import url
    from mysite import views

    urlpatterns = patterns('',
        url(r'^hello$', views.hello),
        url(r'^time$', views.current_datetime)
    )

    urlpatterns += patterns('',
        url(r'^tag$', views.tag)
    )

    # 调试模式中
    if settings.DEBUG:
        urlpatterns += patterns('',
            url(r'^debuginfo$', views.debug)
        )

```

#### 使用命名组

使用命名组可以让你的URLConfs更加清晰，减少搞混参数次序潜在BUG。
命名组失去简洁性，增强可读性。

```python
    urlpatterns += patterns(
        url(r'^articles/(?P<year>\d{4})$', views.yearArchive),
        url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', views.monthArchive)
    )
```

#### 传递额外的参数到视图函数中

使用额外的URLconf参数向视图函数传递额外信息。

```python
    # urls.py

    from django.conf.urls import url
    from mysite import views

    urlpatterns = [
        url(r'^foo$', views.foobar, {'templateName': 'template1.html'}),
        url(r'^bar$', views.foobar, {'templateName': 'template2.html'})
    ]

    # views.py

    from django.shortcuts import render_to_response
    from mysite.models import Book

    def foobar(request, templateName):
        list = Book.objects.filter(is_new = True)
        return render_to_response(templateName, {'list': list})
```

#### 伪造捕捉到的URLconf值

```python
    urlpatterns = [
        url(r'^data/birthday$', views.viewD, {'month': 'jan', 'day': '06'}),
        url(r'^data/(?P<month>\w{3})/(?P<day>\d{2})$', views.viewD)
    ]
```

#### 通用视图

```python
    # urls.py

    from django.conf.urls import url
    from mysite import models, views

    urlpatterns = [
        url(r'^events$', view.objectList, {'model': models.Event}),
        url(r'^blog/entries$', view.objectList, {'model': models.BlogEntry})
    ]

    # views.py

    from django.shortcuts import render_to_response

    def objectList(request, model):
        objectList = model.objects.all()
        template_name = 'mysite/%s_list.html' % model.__name__.lower()
        return render_to_response(template_name, {'objectList': objectList})
```

#### 提供视图配置选项

```python
    def myView(request, templateName):
        var = doSomething()
        return render_to_response(templateName, {'var': var})
```

#### 使用缺省视图参数

```python
    # urls.py

    from django.conf.urls import url
    from mysite import views

    urlpatterns = [
        url(r'^blog$', views.page),
        url(r'^blog/(?P<id>\d+)$', views.page)
    ]

    # views.py

    def page(request, id = '1'):
        pass
```

#### 特殊情况视图处理

URLconf中的一系列URL,需要处理其中某个URL，要使用将URLconf中把特殊情况放在首位的线性处理方式。

```python
    urlpatterns = [
        url(^auth/user/add$, views.userAddStage),
        url(^([^/]+)([^/]+)/add$, views.addStage)
    ]
```

#### 从URL中捕获文本

每个被捕获的参数将作为纯Python字符串发送。

```python
    # urls.py

    from django.conf.urls import url
    from mysite import views

    urlpatterns = [
        url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})$', views.article)
    ]

    # views.py

    def article(request, year, month, day):
        date = datetime.date(int(year), int(month), int(day))
```

#### 包含其他URLconf

```python
    from django.conf.urls import url,include

    urlpatterns = [
        url(r'^books', include('books.urls')),
        url(r'^contact', include('contact.urls'))
    ]
```

#### 视图函数的高级概念

```python
    # urls.py

    from django.conf.urls import url
    from mysite import views

    urlpatterns = [
        url(r'^page$', views.page)
    ]

    # views.py

    from django.http import HttpResponseRedirect, Http404
    from shortcuts import render_to_response

    def page(request):
        if request.method == 'POST':
            doSomething()
            return HttpResponseRedirect('/login')
        elif request.method == 'GET':
            doSomething()
            return render_to_response('page.html')
        else:
            raise Http404()


    ## 优化

    # urls.py

    from django.conf.urls import url
    from mysite import views

    urlpatterns = [
        url(r'^page$', views.page, {'GET': views.get, 'POST': views.post})
    ]

    # views.py

    from django.http import Http404, HttpResponseRedirect
    from django.shortcuts import render_to_response

    def page(request, *args, **kwargs):
        getView = kwargs.pop('GET', None)
        postView = kwargs.pop('POST', None)
        if request.method == 'GET' and getView is not None:
            return getView(request, *args, **kwargs)
        elif request.method == 'POST' and postView is not None:
            return postView(request, *args, **kwargs)
        raise Http404

    def get(request):
        assert request.method == 'GET'
        doSomething()
        return render_to_response('page.html')

    def post(request):
        assert request.method == 'POST'
        doSomething()
        return HttpResponseRedirect('/login')

```

#### 包装视图函数

使用装饰器包装视图函数

```python
    def view1(request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/account/login')
        # ...
        return render_to_response('template1.html')

    def view2(request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/account/login')
        # ...
        return render_to_response('template2.html')

    def view3(request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/account/login')
        # ...
        return render_to_response('template3.html')


    # 使用装饰器

    def requireLogin(func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated():
                return HttpResponseRedirect('/account/login')
            return func(request, *args, **kwargs)
        return wrapper

    # urls.py

    from django.conf.urls import url
    from mysite import views
    from mysite.decorator import requireLogin

    urlpatterns = [
        url(r'^view1$', requireLogin(views.view1)),
        url(r'^view2$', requireLogin(views.view2)),
        # ...
    ]
```

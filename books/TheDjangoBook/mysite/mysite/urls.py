"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from mysite import views
from mysite.decorators import requireLogin

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^hello$', views.hello),
    url(r'^time$', views.currentTime),
    url(r'^time/plus/(\d{1,2})$', views.plusTime),
    url(r'^template$', views.renderTemplate),
    url(r'^ua$', views.UADisplay),
    url(r'^info$', views.requestInfo),
    url(r'^user/(?P<userId>\d+)/info$', requireLogin(views.userInfo)),
    url(r'^login$', views.login),

    url(r'books', include('books.urls')),

    url(r'contact', include('contact.urls'))
]

urlpatterns += [
    url(r'^articles/(?P<year>\d{4})$', views.yearArchive),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', views.monthArchive)
]

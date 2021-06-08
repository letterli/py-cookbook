from django.conf.urls  import url

from contact import views

urlpatterns = [
    url('^$', views.index)
]

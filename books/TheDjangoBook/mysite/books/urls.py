from django.conf.urls import url

from books import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/search/form$', views.searchForm),
    url(r'^/search', views.search),
]


from django.conf.urls import *
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^login/$', views.login, name='index'),
    url('^logout/$', views.logout, name='index'),
    url('^register/$', views.register, name='index'),
]


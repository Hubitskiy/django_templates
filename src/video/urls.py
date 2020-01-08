from django.urls import re_path
from . import views

urlpatterns = [
	re_path('^hello/$', views.hello),
	re_path('^hello/(?P<slug>[-\w]+)/$', views.show_one),
]
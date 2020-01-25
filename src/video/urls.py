from django.urls import re_path
from . import views

urlpatterns = [
	re_path('^hello/$', views.hello, name="hello_url"),
	re_path('^hello/add_comment_blyt/(?P<slug>[-\w]+)/$', views.add_comment, name='add_comment'),
	re_path('^hello/(?P<slug>[-\w]+)/$', views.show_one),
	re_path('^form_comment/(?P<slug>[-\w]+)/$', views.form_comment, name='form_comment'),
	re_path('^form_video_creater/$', views.form_video_creater, name='form_video_creater')
]

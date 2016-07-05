from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'), #tells django that views.post_list is place to visit
												   #when someone enters site at http://127.0.0.1:8000/

	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'), #now able to post_new things
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'), #when edit a blog entry
]
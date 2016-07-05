from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'), #tells django that views.post_list is place to visit
												   #when someone enters site at http://127.0.0.1:8000/
]
from django.conf.urls import url
from . import views


urlpatterns = [
	
	# Posts urls
    url(r'^$', views.posts_list, name='posts_list'),
	url(r'^create/$', views.posts_create, name='posts_create'),
    url(r'^detail/$', views.posts_detail, name='posts_detail'),
    url(r'^update/$', views.posts_update, name='posts_update'),
    url(r'^delete/$', views.posts_delete, name='posts_delete'),


]
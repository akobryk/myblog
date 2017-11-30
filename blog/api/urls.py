from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from blog_auth.views import show_users_profiles
from blog.views import PostMonthArchiveView 
from blog.models import Post
from .views import (
    PostListAPIView, 
    PostRetrieveAPIView, 
    PostUpdateAPIView, 
    PostDeleteAPIView,
    PostCreateAPIView,
)



urlpatterns = [
	
	# Posts urls
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', PostRetrieveAPIView.as_view(), name='retrieve'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),





#     url(r'^$', views.posts_list, name='posts_list'),
#     url(r'^profile/(?P<username>[\w\-]+)/$', login_required(show_users_profiles), name='show_profiles'),
#     url(r'^create/$', login_required(views.posts_create), name='posts_create'),
#     url(r'^(?P<slug>[\w-]+)/$', login_required(views.posts_detail), name='posts_detail'),
#     url(r'^(?P<slug>[\w-]+)/edit/$', login_required(views.posts_update), name='posts_update'),
#     url(r'^(?P<slug>[\w-]+)/delete/$', login_required(views.posts_delete), name='posts_delete'),

#     # Categories, tags, experts, archive
#     url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
#         PostMonthArchiveView.as_view(month_format='%m', template_name='post_archive.html'),
#         name="archive_month_numeric"),
#     url(r'^category/(?P<name>[\w\-]+)/$', views.category, name='category'),
#     url(r'^tag/(?P<name>[\w.\-]+)/$', views.tag, name='tag'),
#     url(r'^expert/(?P<username>[\w\-]+)/$', views.expert, name='expert'),
    

#      # Choose language
#     url(r'^i18n/', include('django.conf.urls.i18n')),

 ]


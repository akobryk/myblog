from django.conf.urls import url, include
from blog_auth.views import show_users_profiles
#from django.views.generic.dates import ArchiveIndexView
from .views import PostMonthArchiveView 
from .models import Post
from . import views



urlpatterns = [
	
	# Posts urls

    url(r'^$', views.posts_list, name='posts_list'),
    url(r'^profile/(?P<username>[\w\-]+)/$', show_users_profiles, name='show_profiles'),
    url(r'^create/$', views.posts_create, name='posts_create'),
    url(r'^(?P<slug>[\w-]+)/$', views.posts_detail, name='posts_detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.posts_update, name='posts_update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.posts_delete, name='posts_delete'),

    # Categories, tags, experts, archive
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        PostMonthArchiveView.as_view(month_format='%m', template_name='post_archive.html'),
        name="archive_month_numeric"),
    url(r'^archive/to-do$', views.posts_archive, name='archive'), # temporary hardcode it
    url(r'^category/(?P<name>[\w\-]+)/$', views.category, name='category'),
    url(r'^tag/(?P<name>[\w.\-]+)/$', views.tag, name='tag'),
    url(r'^expert/(?P<username>[\w\-]+)/$', views.expert, name='expert'),
    

     # Choose language
    url(r'^i18n/', include('django.conf.urls.i18n')),


]


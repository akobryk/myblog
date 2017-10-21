"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static 
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blog.views import contact_admin, about
from blog_auth.views import user_profile_update, user_profile_disable, show_users_profiles
from django.views.generic.base import RedirectView, TemplateView
from registration.backends.default.views import RegistrationView, ActivationView


urlpatterns = [
	# Include posts urls
   url(r'^posts/', include('blog.posts_urls', namespace='posts')),
   
     # Admin url
   url(r'^admin/', admin.site.urls),

   # Contact admin url
   url(r'^contact-admin/$', contact_admin, name='contact_admin'),

   # Ratings 
   url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),

   # "About" url
   url(r'^about/$', about, name='about'),

    # Choose language
   url(r'^i18n/', include('django.conf.urls.i18n')),

   # Social auth
   url('', include('social_django.urls', namespace='social')),

   # User related urls
  # url(r'^users/profile/$', TemplateView.as_view(template_name='registration/profile.html'), name='profile'),
   #url(r'^users/profile/(?P<username>[a-zA-Z0-9]+)/$', show_users_profiles, name='profile_users'),
 # url(r'^users/profile/edit/$', user_profile_update, name='profile_update'),
   url(r'^users/profile/(?P<username>[\w\-]+)/$', show_users_profiles, name='profile_users'),
   url(r'^users/profile/edit/(?P<username>[\w\-]+)/$', user_profile_update, name='profile_update'),
   url(r'^users/profile/disable/(?P<username>[\w\-]+)/$', user_profile_disable, name='profile_dіsable'),
  

   url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'posts:posts_list'}, name='auth_logout'),
   url(r'^register/complete/$', RedirectView.as_view(pattern_name='posts:posts_list'), name='registration_complete'),
   url(r'register/activation-complete/$', RedirectView.as_view(pattern_name='posts:posts_list'), 
       name='registration_activation_complete'),
  
   url(r'^users/', include('registration.backends.default.urls')),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
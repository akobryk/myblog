from django.conf.urls import url
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

]
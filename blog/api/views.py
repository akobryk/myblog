from django.db.models import Q
from rest_framework.filters import (
	SearchFilter, OrderingFilter,)
from rest_framework.generics import (
	ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView,)
from rest_framework.permissions import (
	AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly,)
from .pagination import PostPageNumberPagination
from .permissions import IsOwnerOrReadOnly
from blog.models import Post
from .serializers import (
	PostListSerializer, PostRetrieveSerializer, PostCreateUpdateSerializer,)


class PostListAPIView(ListAPIView):
	serializer_class = PostListSerializer
	permission_classes = [AllowAny]
	filter_backends = [SearchFilter, OrderingFilter]
	pagination_class = PostPageNumberPagination
	search_fields = [
		'title',
		'content',
		'user__first_name',
		'user__last_name',
		'user__username',
		'tag__name',
		'category__name',
	]


	def get_queryset(self, *args, **kwargs):
		queryset_list = Post.objects.all()
		s = self.request.GET.get('s')
		if s:
			queryset_list = queryset_list.filter(
				Q(title__icontains=s) |
				Q(content__icontains=s) |
				Q(user__first_name__icontains=s) |
				Q(user__last_name__icontains=s) |
				Q(user__username__icontains=s) |
				Q(tag__name__icontains=s) |
				Q(category__name__icontains=s)
				).distinct()
		return queryset_list

class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	permission_classes = [IsAuthenticated, IsAdminUser]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class PostRetrieveAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostRetrieveSerializer
	lookup_field = 'slug'
	permission_classes = [IsAuthenticated]

class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	lookup_field = 'slug'
	permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)


class PostDeleteAPIView(DestroyAPIView):
	permission_classes = [IsAdminUser, IsOwnerOrReadOnly]
	queryset = Post.objects.all()
	serializer_class = PostRetrieveSerializer
	lookup_field = 'slug'

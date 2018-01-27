from rest_framework.serializers import (
	ModelSerializer, HyperlinkedIdentityField, SerializerMethodField)
from blog.models import Post

class PostListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name='posts_api:retrieve', 
		lookup_field='slug'
		)
	delete_url = HyperlinkedIdentityField(
		view_name='posts_api:delete',
		lookup_field='slug'
		)
	user = SerializerMethodField()
	image = SerializerMethodField()
	markdown_html = SerializerMethodField()
	class Meta:
		model = Post
		fields = [
			'url',
			'user',
			'title',
			'content',
			'markdown_html',
			'image',
			'delete_url',
			
			]
	def get_markdown_html(self, obj):
		return obj.get_markdown()

	def get_user(self, obj):
		user = obj.user.get_full_name()
		if not user:
			user = obj.user.username
		return str(user)

	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image


class PostRetrieveSerializer(ModelSerializer):
	delete_url = HyperlinkedIdentityField(
		view_name='posts_api:delete',
		lookup_field='slug'
		)
	user = SerializerMethodField()
	image = SerializerMethodField()
	markdown_html = SerializerMethodField()
	class Meta:
		model = Post
		fields = [
			'user',
			'id',
			'title',
			'slug',
			'content',
			'markdown_html',
			'publish',
			'delete_url',
			]
	def get_markdown_html(self, obj):
		return obj.get_markdown()
	def get_user(self, obj):
		user = obj.user.get_full_name()
		if not user:
			user = obj.user.username
		return str(user)

	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image

class PostCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'title',
			'content',
			'publish',
			'draft',

			]
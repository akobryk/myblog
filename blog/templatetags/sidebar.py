from django import template
import time
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Count, IntegerField, Sum, Case, When
from ..models import Tag, Category, Post



register = template.Library()

@register.inclusion_tag('sidebar_nav.html')
def sidebar_nav():
	"""
	Creating a sidebar for a blog with:
		-social links;
		-categories;
		-last posts;
		-experts;
		-popular posts;
		-an archive of posts;
		-tags.

	"""
	#  creating an archive of posts
	archive = Post.objects.active().dates('publish', 'month')
	for months in archive:
		Post.objects.filter(publish__year=months.year, publish__month=months.month)
		# making a tuple for an iteration
		months = (months,)

	# all tags
	tags = Tag.objects.all()

	# active post count for categories and experts
	active_post_count = Sum(Case(When(
	    post__publish__lte=timezone.now(), post__draft=False, then=1), default=0, output_field=IntegerField()))

	# all categories
	categories = Category.objects.order_by('name').annotate(count_posts=active_post_count)

	# filtering top 5 posts
	top_five = Post.objects.active().filter(ratings__isnull=False).order_by('-ratings__average')[:5]
	# filtering six latest posts
	new_posts = Post.objects.active().values('id', 'title', 'slug').order_by('-datetime_stamp')[:6]
	# filtering experts with the biggest count of posts

	experts = User.objects.annotate(count_experts=active_post_count).order_by('-count_experts')[:6]

	return {'tags': tags,
			'categories': categories,
			'new_posts': new_posts,
			'experts': experts,
			'top_five': top_five,
			'archive': archive,
		}
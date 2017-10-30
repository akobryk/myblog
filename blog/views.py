from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from .utils import paginate, get_read_time
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.db.models import Q
from django.core.mail import send_mail

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from django.views.generic.dates import MonthArchiveView

from .models import Post, Category, Tag
from .forms import PostForm, ContactAdminForm
from django.conf import settings
from django.core.exceptions import PermissionDenied
import logging

# Create your views here.
@login_required
def posts_create(request):
	#if not request.user.is_staff or not request.user.is_superuser:
		#raise Http404

	form = PostForm(request.POST or None, request.FILES or None, user=request.user)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		form.save_m2m()
		messages.success(request, _('Successfully Created Post!'))
		return HttpResponseRedirect(instance.get_absolute_url())


	context = {
		'form': form,
	}
	return render(request, 'post_create_update.html', context)

# Retrieve
@login_required
def posts_detail(request, slug=None):
	today = timezone.now().date()

	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > today or instance.draft:
		if not request.user.is_staff and not request.user.is_superuser:
			if request.user != instance.user:
				raise Http404
	context = {
		'title': instance.title,
		'instance': instance,
		'today': today,


	}
	return render(request, 'post_detail.html', context)

# List items
def posts_list(request):
	today = timezone.now().date()

	queryset_list = Post.objects.active()

	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()
	elif request.user.is_anonymous:
		queryset_list = Post.objects.active()
	else:
		queryset_list = Post.objects.active() | Post.objects.all().select_related().filter(user=request.user)





	search = request.GET.get('search')
	if search:
		queryset_list = queryset_list.filter(
			Q(title__icontains=search) |
			Q(content__icontains=search) |
			Q(user__first_name__icontains=search) |
			Q(user__last_name__icontains=search) |
			Q(user__username__icontains=search) |
			Q(tag__name__icontains=search) |
			Q(category__name__icontains=search)
			).distinct()

	context = paginate(queryset_list, 6, request, {
		'title': 'List',
		'today': today,
	}, var_name='object_list')
	return render(request, 'posts_list.html', context)


# Post update
@login_required
def posts_update(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if not request.user.is_staff or not request.user.is_superuser:
		if request.user != instance.user:
			raise Http404
	form = PostForm(request.POST or None, request.FILES or None, instance=instance, user=request.user)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		form.save_m2m()
		messages.success(request, _('Successfully Updated Post!'))
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'title': instance.title,
		'instance': instance,
		'form': form,
	}
	return render(request, 'post_create_update.html', context)
@login_required
def posts_delete(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if not request.user.is_staff or not request.user.is_superuser:
		if request.user != instance.user:
			raise Http404
	if request.method == 'POST':
		instance.delete()
		messages.success(request, _('Post has been successfully deleted!'))
		return redirect('posts:posts_list')
	context = {
		'title': instance.title,
		'instance': instance,
		'slug': slug,
	}
	return render(request, 'posts_delete.html', context)

# Contact admin
def contact_admin(request):
	# check if form was posted:
	if request.method == 'POST':
		# create a form instance and populate it with data
			# from the request
		form = ContactAdminForm(request.POST or None)

		# check whether the user data is valid:
		if form.is_valid():
			# send an email
			form_name = form.cleaned_data['name']
			form_email = form.cleaned_data['email']
			form_subject = form.cleaned_data['subject']
			form_message = form.cleaned_data['message']
			via = 'Contact email'

			from_email = settings.EMAIL_HOST_USER
			to_email = [from_email, 'a.kobryk@gmail.com']

			contact_message = '%s: \n%s \n%s: %s' % (form_name, form_message, via, form_email)
			try:
				send_mail(form_subject,
					contact_message,
					from_email,
					to_email,
					fail_silently=False)
			except Exception:
				error_message = _('The error has been occured. Please, try later!')
				message = messages.error(request, error_message)
				logger = logging.getLogger(__name__)
				logger.exception(error_message)
			else:
				messages.success(request, _('The message has been delivered!'))

			return redirect('contact_admin')

	else:
		form = ContactAdminForm()

	return render(request, 'contact_admin_form.html', {'form': form})

def tag(request, name=None):
	tag = Tag.objects.select_related().get(name=name)
	posts = tag.post_set.active()
	context = {
		'tag': tag,
		'posts': posts,
	}
	return render(request, 'tags.html', context)

def category(request, name=None):
	category = Category.objects.select_related().get(name=name)
	posts = category.post_set.active()
	context = {
		'category': category,
		'posts': posts,
	}
	return render(request, 'categories.html', context)

def expert(request, username=None):
	expert = User.objects.select_related().get(username=username)
	posts = expert.post_set.active()
	context = {
		'expert': expert,
		'posts': posts,
	}
	return render(request, 'experts.html', context)

def posts_archive(request):
	# TODO: create a decent archive for posts
	archive = Post.objects.active().order_by('-publish')
	context = {
		'archive': archive,
	}
	return render(request, 'archive.html', context)

def about(request):
	return render(request, 'about.html', {})

# Posts archive
class PostMonthArchiveView(MonthArchiveView):
	queryset = Post.objects.active()
	date_field = 'publish'
	allow_fututre = False

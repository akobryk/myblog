from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm, ProfileForm
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
# Create your views here.

@login_required
def user_profile_update(request, username=None):
	instance_form = User.objects.get(username=username)
	if not request.user.is_staff or not request.user.is_superuser:
		if request.user.username != instance_form.username:
			raise Http404
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=instance_form)
		profile_form = ProfileForm(request.POST, request.FILES,
		 	instance=request.user.userprofile)
		
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, _('Profile successfully updated!'))
			return redirect('posts:posts_list')
		else: 
			messages.error(request, _('Please correct errors below!'))
	else:
		user_form = UserForm(instance=instance_form)
		profile_form = ProfileForm(instance=request.user.userprofile)
		
	context = {
		'instance': instance_form,
		'user_form': user_form,
		'profile_form': profile_form,
	}
	return render(request, 'registration/profile_update.html', context)

@login_required
def show_users_profiles(request, username):
	try:
		user_pr = User.objects.get(username=username)
	except DoesNotExist:
		raise Http404

	return render(request, 'registration/profile.html', {'user_pr': user_pr})

@login_required
def user_profile_disable(request, username=None):
	instance = User.objects.get(username=username)
	if request.method == 'POST':
		instance.is_active = False
		instance.save()
		messages.success(request, 'Profile successfully disabled!')
		return redirect('posts:posts_list')
	context = {
		'instance': instance,
	}
	return render(request, 'registration/profile_disable.html', context)
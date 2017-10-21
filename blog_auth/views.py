from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm, ProfileForm
# Create your views here.


# def user_profile_update(request):
# 	if request.method == 'POST':
# 		user_form = UserForm(request.POST, instance=request.user)
# 		profile_form = ProfileForm(request.POST, request.FILES,
# 		 	instance=request.user.userprofile)
# 		if user_form.is_valid() and profile_form.is_valid():
# 			user_form.save()
# 			profile_form.save()
# 			messages.success(request, 'Successfully Updated Profile!')
# 			return redirect('profile')
# 		else: 
# 			message.error(request, 'Please, correct errors below!')
# 	else:
# 		user_form = UserForm(instance=request.user)
# 		profile_form = ProfileForm(instance=request.user.userprofile)
		
# 	context = {
# 		'user_form': user_form,
# 		'profile_form': profile_form,
# 	}
# 	return render(request, 'registration/profile_update.html', context)


def user_profile_update(request, username=None):
	instance_form = User.objects.get(username=username) 
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=instance_form)
		profile_form = ProfileForm(request.POST, request.FILES,
		 	instance=request.user.userprofile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Profile successfully updated!')
			return redirect('posts:posts_list')
			
		else: 
			messages.error(request, 'Please, correct errors below!')
	else:
		user_form = UserForm(instance=instance_form)
		profile_form = ProfileForm(instance=request.user.userprofile)
		
	context = {
		'instance': instance_form,
		'user_form': user_form,
		'profile_form': profile_form,
	}
	return render(request, 'registration/profile_update.html', context)


def show_users_profiles(request, username):
	try:
		user_pr = User.objects.get(username=username)
	except DoesNotExist:
		raise Http404
	return render(request, 'registration/profile.html', {'user_pr': user_pr})


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
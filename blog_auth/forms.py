from django import forms 
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
	class Meta(object):
		model = User
		fields = [
			'username',
			'email',
			'first_name',
			'last_name',
		]

class ProfileForm(forms.ModelForm):
	class Meta(object):
		model = UserProfile
		fields = [
			'avatar',
			'mobile_phone',
			'skype',
			'birthday',
			'about_me',
		]
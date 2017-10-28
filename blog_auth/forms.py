from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail
from django.utils.translation import ugettext_lazy as _
from .models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from captcha.fields import CaptchaField



class UserForm(forms.ModelForm):
	class Meta(object):
		model = User
		fields = [
			'username',
			'email',
			'first_name',
			'last_name',
		]

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		
		self.helper = FormHelper()
		
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 col-form-label'
		self.helper.field_class = 'col-sm-4'



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

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()

		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 col-form-label'
		self.helper.field_class = 'col-sm-4'



class LoginCaptchaForm(AuthenticationForm):
	captcha = CaptchaField(label=_('I`m not a robot'))


class RegistrationViewUniqueEmail(RegistrationView):
	form_class = RegistrationFormUniqueEmail
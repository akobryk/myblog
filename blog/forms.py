from django import forms
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from pagedown.widgets import PagedownWidget
from .models import Post
from django.contrib.auth.models import User
from modeltranslation.forms import TranslationModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PostForm(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget(show_preview=False))
	publish = forms.DateField(widget=forms.SelectDateWidget)
	class Meta(object):
		model = Post
		fields = [
			'title',
			'content', 
			'image',  
			'publish', 
			'category', 
			'tag',
			'draft',
		]

	def __init__(self, *args, **kwargs):
		draft = kwargs.pop('draft', None)
		user = kwargs.pop('user', None)
		super(PostForm, self).__init__(*args, **kwargs)
		if not user.is_staff or not user.is_superuser:
			self.fields['draft'].widget.attrs['hidden'] = True


class ContactAdminForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(ContactAdminForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()

		# tag attributes
		self.helper.form_class = ''
		self.helper.form_method = 'post'
		self.helper.form_action = reverse('contact_admin')

		# bootstrap styles
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 col-form-label'
		self.helper.field_class = 'col-sm-4'

		# buttons 
		self.helper.add_input(Submit('send_button', _('Send'), css_class='btn btn-info'))

	name = forms.CharField(
		max_length=160,
		label='Your Name')
	email = forms.EmailField(
		label='Your Email')
	subject = forms.CharField(
		label='Title',
		max_length=128)
	message = forms.CharField(
		label='Message text',
		max_length=2560,
		widget=forms.Textarea)
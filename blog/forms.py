from captcha.fields import CaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from pagedown.widgets import PagedownWidget


from django import forms
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from .models import Post


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
        # draft = kwargs.pop('draft', None)
        user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)
        if not user.is_staff or not user.is_superuser:
            self.fields['draft'].widget.attrs['hidden'] = True
            # self.fields['draft'].label = False


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
        self.helper.label_class = 'col-sm-4 col-form-label'
        self.helper.field_class = 'col-sm-8'

        # buttons
        self.helper.add_input(
            Submit('send_button', _('Send'), css_class='btn btn-info'))

    name = forms.CharField(
        max_length=160,
        label=_('Your Name'))
    email = forms.EmailField(
        label=_('Your Email'))
    subject = forms.CharField(
        label=_('Title'),
        max_length=128)
    message = forms.CharField(
        label=_('Message text'),
        max_length=2560,
        widget=forms.Textarea)
    not_a_robot = CaptchaField(
        label=_('I`m not a robot'))

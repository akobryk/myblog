from modeltranslation.translator import register, TranslationOptions
from django.contrib.auth.models import User
from .models import UserProfile

@register(User)
class UserTranslationOptions(TranslationOptions):
	fields = ('first_name', 'last_name',)

@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
	fields = ('about_me',)

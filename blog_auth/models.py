from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
	""" To keep extra user data """ 
	# user mapping 
	user = models.OneToOneField(User)

	class Meta(object):
		verbose_name = _('User Profile')

	# extra user data 
	avatar = models.ImageField(
		null=True,
		blank=True,
		verbose_name=_('Photo'))

	birthday = models.DateField(
		null=True,
		blank=True,
		verbose_name=_('Date of birthday'))

	mobile_phone = models.CharField(
		max_length=12,
		blank=True,
		verbose_name=_('Mobile Phone'),
		default='')

	skype = models.CharField(
		max_length=120,
		blank=True,
		verbose_name='Skype')

	about_me = models.TextField(
		blank=True,
		verbose_name=_('About me')
		)


	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.userprofile.save()
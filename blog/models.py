from django.db import models


# Create your models here.

class Post(models.Model):
	""" Post model """ 

	class Meta(object):
		verbose_name = 'Title'
		verbose_name_plural = 'Titles'

	title = models.CharField(max_length=255, verbose_name ='Title')
	photo = models.ImageField(verbose_name='Photo')
	date_time = models.DateTimeField(verbose_name="The date of publication")
	content = models.TextField(max_length=10000)

	def __str__(self):
		return '%s' % (self.title)
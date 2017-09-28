from django.db import models


# Create your models here.

class Post(models.Model):

	title = models.CharField(
		max_length=120)
	content = models.TextField()
	updated= models.DateTimeField(
		auto_now=True,
		auto_now_add=False)
	datetime_stamp = models.DateTimeField(
		auto_now=False,
		auto_now_add=True)

	def __str__(self):
		return "%s" % self.title



# Define CRUD. Create, Read, Update, and Delete // It`s about CRUD and List / Search
from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'datetime_stamp', 'updated']
	list_display_links = ['datetime_stamp', 'updated']
	list_editable = ['title']
	list_filter = ['datetime_stamp', 'updated']
	search_fields = ['title', 'content']

	class Meta:
		model = Post



# Register your models here.
admin.site.register(Post, PostAdmin)
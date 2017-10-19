from django.contrib import admin
from django.db import models
from .models import Post, Category, Tag
from pagedown.widgets import AdminPagedownWidget

class PostAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': AdminPagedownWidget()},
	}
	ordering = ['datetime_stamp']
	list_display = ['title', 'datetime_stamp', 'updated']
	list_display_links = ['datetime_stamp', 'updated']
	list_editable = ['title']
	list_filter = ['datetime_stamp', 'updated']
	search_fields = ['title', 'content']
	list_per_page = 12

	class Meta:
		model = Post

class TagAdmin(admin.ModelAdmin):
	list_display_links = None
	list_display = ['name']
	list_editable = ['name']
	list_per_page = 12

	class Meta:
		model = Tag

class CategoryAdmin(admin.ModelAdmin):
	list_display_links = None
	list_display = ['name']
	list_editable = ['name']
	list_per_page = 12

	class Meta:
		model = Category

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
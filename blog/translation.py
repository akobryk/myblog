from modeltranslation.translator import register, TranslationOptions
from .models import Post
from .forms import PostForm

@register(Post)
class PostTranslationOptions(TranslationOptions):
	fields = ('title', 'content',)


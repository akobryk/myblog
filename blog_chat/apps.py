from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class BlogChatConfig(AppConfig):
    name = 'blog_chat'
    verbose_name = _('Blog chat')

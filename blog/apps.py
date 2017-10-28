from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class BlogAppConfig(AppConfig):
    name = 'blog'
    verbose_name = _('Blog')

    def ready(self):
    	from blog import signals
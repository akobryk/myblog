from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class ChatMessage(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User')
        )
    message = models.TextField(
        max_length=3000,
        verbose_name=_('Message'))
    message_html = models.TextField(
        verbose_name=_('Message html'))
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created'))
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated'))

    class Meta:
        verbose_name = _('Chat Message')
        verbose_name_plural = _('Chat Messages')

    def __str__(self):
        return self.message

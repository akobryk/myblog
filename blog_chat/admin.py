from django.contrib import admin
from .models import ChatMessage
from .forms import AdminChatMessageForm


class ChatMessageAdmin(admin.ModelAdmin):
    class Meta:
        model = ChatMessage

    form = AdminChatMessageForm
    ordering = ['created']
    search_field = ['message']
    list_per_page = 15
    list_display_links = ['user', 'message']
    list_display = [
        'user',
        'message',
        'updated',
        'created',
    ]


admin.site.register(ChatMessage, ChatMessageAdmin)

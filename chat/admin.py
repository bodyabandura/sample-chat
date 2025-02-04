from django.contrib import admin
from .models import ChatUser, Chat, Message

admin.site.register(ChatUser)
admin.site.register(Chat)
admin.site.register(Message)

from django.contrib import admin
from .models import Message, Chatroom, Channel

# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass

@admin.register(Chatroom)
class ChatroomAdmin(admin.ModelAdmin):
    pass

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    pass

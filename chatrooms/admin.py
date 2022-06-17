from django.contrib import admin
from .models import Chatroom


# Register your models here.
class AdminChatroom(admin.ModelAdmin):
    list_display = (
        'name',
        'subject',
    )


admin.site.register(Chatroom, AdminChatroom)

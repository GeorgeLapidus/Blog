from django.contrib import admin
from account.models import BlogUser


class BlogUserAdmin(admin.ModelAdmin):
    """Отредактированный для админки класс BlogUser"""
    list_display = ('username', 'email', "send_message", 'date_joined')
    list_filter = ('send_message', 'date_joined')

admin.site.register(BlogUser, BlogUserAdmin)

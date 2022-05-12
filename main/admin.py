from django.contrib import admin

# Register your models here.
from main.models import Category, Post, Comment, PostAdditionalImage, Emails


class PostAdditionalImageInline(admin.TabularInline):
    """Класс для добавления в админке поля с дополнительными изображениями к модели Post"""
    model = PostAdditionalImage


class PostAdmin(admin.ModelAdmin):
    """Отредактированный для админки класс Post с возможностью прикреплять дополнительные изображения"""
    list_display = ('category', 'title', 'description', 'briefdescription', 'image', 'author', 'likes', 'views')
    fields = ('category', 'title', 'description', 'briefdescription', 'image', 'author', 'likes', 'views')
    inlines = (PostAdditionalImageInline,)


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Emails)
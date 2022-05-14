from django.contrib import admin

# Register your models here.
from main.models import Category, Post, Comment, PostAdditionalImage, Emails, AnswerComment, Like


class PostAdditionalImageInline(admin.TabularInline):
    """Класс для добавления в админке поля с дополнительными изображениями к модели Post"""
    model = PostAdditionalImage


class PostAdmin(admin.ModelAdmin):
    """Отредактированный для админки класс Post с возможностью прикреплять дополнительные изображения"""
    list_display = ('title', 'category', 'description', 'briefdescription', 'likes', 'views', 'created', 'updated', 'image', 'author')
    inlines = (PostAdditionalImageInline,)


class LikeAdmin(admin.ModelAdmin):
    """Отредактированный для админки класс Like для отображения нужных полей"""
    list_display = ('post', 'category', 'user', 'created', 'id')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(AnswerComment)
admin.site.register(Emails)
admin.site.register(Like, LikeAdmin)
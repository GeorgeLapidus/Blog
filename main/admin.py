from django.contrib import admin

# Register your models here.
from main.models import Category, Post, Comment, PostAdditionalImage, Emails, AnswerComment


class PostAdditionalImageInline(admin.TabularInline):
    """Класс для добавления в админке поля с дополнительными изображениями к модели Post"""
    model = PostAdditionalImage


class PostAdmin(admin.ModelAdmin):
    """Отредактированный для админки класс Post с возможностью прикреплять дополнительные изображения"""
    fields = ('title', 'category', 'description', 'briefdescription', 'image', 'author')
    list_display = ('title', 'category', 'description', 'briefdescription', 'likes', 'views', 'created', 'updated',
                    'image', 'author')
    inlines = (PostAdditionalImageInline,)


class CommentAdmin(admin.ModelAdmin):
    """Класс для админки модели Comment"""
    list_display = ('text', 'post', 'date_created', 'is_publish')
    list_filter = ('is_publish',)
    list_editable = ('is_publish',)

class AnswerCommentAdmin(admin.ModelAdmin):
    """Класс для админки модели AnswerComment"""
    list_display = ('text', 'comment', 'date_created', 'is_publish')
    list_filter = ('is_publish',)
    list_editable = ('is_publish',)


# from main.models import View, Like
# class ViewAdmin(admin.ModelAdmin):
#     """Отредактированный для админки класс View для отображения нужных полей"""
#     list_display = ('post', 'category', 'user', 'created', 'id')
#
#
# class LikeAdmin(admin.ModelAdmin):
#     """Отредактированный для админки класс Like для отображения нужных полей"""
#     list_display = ('post', 'category', 'user', 'created', 'id')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(AnswerComment, AnswerCommentAdmin)
admin.site.register(Emails)
# admin.site.register(View, ViewAdmin)
# admin.site.register(Like, LikeAdmin)

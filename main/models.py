from django.conf import settings
from django.db import models
from django.urls import reverse
from account.models import BlogUser
# from blog import settings


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    briefdescription = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images', blank=True)
    author = models.CharField(max_length=200, blank=True)
    like = models.IntegerField(default=0, blank=True)
    view = models.IntegerField(default=0, blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:post_detail', args=[self.id])


class Comment(models.Model):
    """Класс комментария к новости"""
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Новость')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    text = models.TextField(verbose_name='Оставить свой комментарий')
    is_publish = models.BooleanField(default=False, verbose_name='Опубликовать на сайте')
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-is_publish', 'date_created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Emails(models.Model):
    """Класс для хранения электронных адресов пользователей, которые хотят получать уведомления о новых постах"""
    email = models.EmailField(blank=False)
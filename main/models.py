from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
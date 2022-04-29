from django.contrib import admin

# Register your models here.
from main.models import Category, Post

admin.site.register(Category)
admin.site.register(Post)
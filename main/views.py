from django.shortcuts import render

# Create your views here.
from main.models import Category, Post


def start_page(request):
    categories = Category.objects.all()

    posts = Post.objects.all()

    context = {'categories': categories, 'posts': posts}

    return render(request, 'start_page.html', context)

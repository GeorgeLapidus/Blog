from django.shortcuts import render, get_object_or_404

# Create your views here.
from main.models import Category, Post


def start_page(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    context = {'categories': categories, 'posts': posts}
    return render(request, 'start_page.html', context)


def post_detail(request, id):
    categories = Category.objects.all()
    post = get_object_or_404(Post, id=id)
    context = {'categories': categories, 'post': post}
    return render(request, 'post_detail.html', context)


def category_post(request, category_id):
    categories = Category.objects.all()
    posts = Post.objects.filter(category_id=category_id)
    context = {'categories': categories, 'posts': posts}
    return render(request, "category_post.html", context)
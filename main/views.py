from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import CommentForm
from .models import Category, Post, Comment


def start_page(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    context = {'categories': categories, 'posts': posts}
    return render(request, 'start_page.html', context)


def post_detail(request, id):
    categories = Category.objects.all()
    post = Post.objects.get(id=id)
    form = CommentForm()
    if request.method == 'POST':
        comment = Comment(text=request.POST.get("text"), post_id=id)
        print (comment)
        comment.save()
        return render(request, 'success_add_comment.html')


    context = {'categories': categories, 'post': post, 'form':form}
    return render(request, 'post_detail.html', context)


def category_post(request, category_id):
    categories = Category.objects.all()
    posts = Post.objects.filter(category_id=category_id)
    context = {'categories': categories, 'posts': posts}
    return render(request, "category_post.html", context)
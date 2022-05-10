from django.shortcuts import render, get_object_or_404

# Create your views here.
from account.models import BlogUser
from .forms import CommentForm, EmailsForm
from .models import Category, Post, Comment, Emails


def start_page(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    form = EmailsForm()
    if request.method == 'POST':
        new_email = EmailsForm(request.POST)
        if new_email.is_valid():
            new_email.save()
            return render(request, 'start_page.html', {'categories': categories, 'posts': posts, 'form': form,'message': "Ваш email сохранен!"})
    context = {'categories': categories, 'posts': posts, 'form': form}
    return render(request, 'start_page.html', context)


def post_detail(request, id):
    categories = Category.objects.all()
    post = Post.objects.get(id=id)
    form = CommentForm()
    comments = Comment.objects.filter(is_publish='True', post_id=id)
    if request.method == 'POST':
        comment = Comment(text=request.POST.get("text"), post_id=id)
        comment.save()
        return render(request, 'success_add_comment.html')


    context = {'categories': categories, 'post': post, 'form':form, 'comments': comments}
    return render(request, 'post_detail.html', context)


def category_post(request, category_id):
    categories = Category.objects.all()
    posts = Post.objects.filter(category_id=category_id)
    context = {'categories': categories, 'posts': posts}
    return render(request, "category_post.html", context)

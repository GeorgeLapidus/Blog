from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, get_object_or_404
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
    comments = Comment.objects.filter(is_publish='True', post_id=id)
    if request.method == 'POST':
        comment = Comment(text=request.POST.get("text"), post_id=id)
        comment.save()
        return render(request, 'success_add_comment.html')
    context = {'categories': categories, 'post': post, 'form':form, 'comments': comments}
    return render(request, 'post_detail.html', context)




# import telebot
# bot = telebot.TeleBot('5344465413:AAGG8i1-QKfIoQTzfEjQVB8pb9YAxZVp9Mw')
# CHANNEL_NAME = '@https://t.me/+CJtzLP2spNk5YjIy'

@receiver(post_save, sender=Comment)
def send_bot_message(sender, **kwargs):
    print("Оставили комментарий")

    # bot.send_message(CHANNEL_NAME, "Оставили комментарий")



def category_post(request, category_id):
    categories = Category.objects.all()
    posts = Post.objects.filter(category_id=category_id)
    context = {'categories': categories, 'posts': posts}
    return render(request, "category_post.html", context)
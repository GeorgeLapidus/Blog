from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from .models import Category, Post, Comment, BlogUser
from .serializers import CategorySerializer, PostSerializer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def start_page(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    context = {'categories': categories, 'posts': posts}
    return render(request, 'start_page.html', context)

def post_detail(request, id):
    """Фукция вывода детальной информации новости"""

    categories = Category.objects.all()
    post = Post.objects.get(id=id)
    form = CommentForm()
    comments = Comment.objects.filter(is_publish='True', post_id=id)
    if request.user.username:
        user = BlogUser.objects.get(username=request.user.username)
        if request.method == 'POST':
            comment = Comment(text=request.POST.get("text"), post_id=id, user=user)
            comment.save()
            return render(request, 'success_add_comment.html')
    context = {'categories': categories, 'post': post, 'form': form, 'comments': comments}
    return render(request, 'post_detail.html', context)


# import telebot
# bot = telebot.TeleBot('5344465413:AAGG8i1-QKfIoQTzfEjQVB8pb9YAxZVp9Mw')
# CHANNEL_NAME = '@https://t.me/+CJtzLP2spNk5YjIy'

@receiver(post_save, sender=Comment)
def send_bot_message(sender, **kwargs):
    """Сигнал об оставленном комментарии"""

    print("Оставили комментарий")
    # bot.send_message(CHANNEL_NAME, "Оставили комментарий")

    send_mail(
        'Оставили комментарий',
        'Вам оставили комментарий на БЛОГ ITECH http://127.0.0.1:8000/',
        'python.project2012@gmail.com',
        ['python.project2012@gmail.com', 'shvedovska_vera@mail.ru'],
        fail_silently=False)
    print("Письмо отправлено с помощью сигнала")



def category_post(request, category_id):
    categories = Category.objects.all()
    posts = Post.objects.filter(category_id=category_id)
    context = {'categories': categories, 'posts': posts}
    return render(request, "category_post.html", context)


@api_view(['GET'])
def api_category(request):
    """api_rest вывод всех категорий блога"""

    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_post(request):
    """api_rest вывод всех новостей"""

    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_category_post(request):
    """api_rest вывод новостей по категориям"""

    categories = Category.objects.all()
    spisok = []
    for i in categories:
        serializer = CategorySerializer(i)
        rez = dict(serializer.data)
        rez['posts'] = [PostSerializer(c).data for c in i.post_set.all()]
        spisok.append(rez)
    return Response(spisok)

@api_view(['GET'])
def api_comments(request):
    """api_rest вывод всех комментариев"""

    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_post_comments(request):
    """api_rest вывод комментариев к новости"""

    posts = Post.objects.all()
    spisok = []
    for i in posts:
        serializer = PostSerializer(i)
        rez = dict(serializer.data)
        rez['comments'] = [CommentSerializer(c).data for c in i.comment_set.all()]
        spisok.append(rez)
    return Response(spisok)
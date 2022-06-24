import generics as generics
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect
# from rest_framework.views import APIView
from rest_framework import generics

from account.models import BlogUser
from .forms import CommentForm, EmailsForm, AnswerCommentForm
from .models import Category, Post, Comment, Emails, AnswerComment, View, Like
# from .serializers import CategoryModelSerializer, PostModelSerializer, CommentModelSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .serializers import CategorySerializer, PostSerializer, PostsAllSerializer, CategoryDetailSerializer, \
    PostDetailedSerializer, SimilarRandomPostsSerializer


def start_page(request):
    """Функция вывода стартовой страницы"""

    categories = Category.objects.all()
    posts = Post.objects.all()
    form = EmailsForm()
    if request.method == 'POST':
        new_email = EmailsForm(request.POST)
        if new_email.is_valid():
            new_email.save()
            return render(request, 'start_page.html',
                          {'categories': categories, 'posts': posts, 'form': form, 'message': "Ваш email сохранен!"})
    context = {'categories': categories, 'posts': posts, 'form': form}
    return render(request, 'start_page.html', context)


def post_detail(request, id):
    """Фукция вывода детальной информации статьи"""
    categories = Category.objects.all()
    post_info = Post.objects.filter(id=id)
    post = post_info[0]
    post_additional_images = post.postadditionalimage_set.all()
    category_id = post.category_id
    user = request.environ['HTTP_COOKIE']

    'Показ 3-ёх случайных похожих статей'
    category_random_posts = Post.objects.filter(category_id=category_id).exclude(id=id).order_by('?')[:3]

    'Счётчик просмотров'
    if request.method == 'GET':
        view = View.objects.filter(post_id=id, user=user)
        if not view:
            view = View(post_id=id, category_id=category_id, user=user)
            view.save()
            post.views += 1
            post_info.update(views=post.views)

    form = CommentForm()
    comments = Comment.objects.filter(is_publish='True', post_id=id)
    answer_comments = AnswerComment.objects.filter(is_publish='True')

    if request.method == 'POST':
        'Счётчик лайков'
        if request.POST.get('Likes'):
            like = Like.objects.filter(post_id=id, user=user)
            if like:
                like.delete()
                post.likes -= 1
            else:
                like = Like(post_id=id, category_id=category_id, user=user)
                like.save()
                post.likes += 1
            post_info.update(likes=post.likes)
        else:
            comment = Comment(text=request.POST.get("text"), post_id=id)
            comment.save()
        return redirect(post.get_absolute_url())
    context = {'categories': categories, 'post': post, 'post_additional_images': post_additional_images, 'form': form,
               'comments': comments, 'answer_comments': answer_comments, 'category_random_posts': category_random_posts}
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
        ['python.project2012@gmail.com'],
        fail_silently=False)
    print("Письмо отправлено с помощью сигнала - оставили комментарий")


@receiver(post_save, sender=Post)
def listen_to_posts(sender, **kwargs):
    """Сигнал для отправки уведомлений о выходе нового поста"""

    emails_form = Emails.objects.all()
    emails_register = BlogUser.objects.filter(send_message=True).exclude(is_superuser=True)
    a = []
    if emails_form:
        for e in emails_form:
            a.append(e.email)
    if emails_register:
        for e in emails_register:
            a.append(e.email)
    recipients = list(set(a))
    subject = 'Новый пост в БЛОГЕ компании ITEC'
    # html_message = render_to_string('message.html')
    # plain_message = strip_tags(html_message)
    plain_message = "Новый пост на сайте айтек"
    from_email = 'python.project2012@gmail.com'
    # send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    send_mail(subject, plain_message, from_email, recipients)
    print("Рассылка уведомлений")


def answer_comment(request, id):
    """Функция ответа на комментарий"""

    form = AnswerCommentForm()
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        answer_comment = AnswerComment(text=request.POST.get("text"), comment_id=id)
        answer_comment.save()
        comment = Comment.objects.get(id=answer_comment.comment_id)
        post = Post.objects.get(id=comment.post_id)
        return redirect(post.get_absolute_url())
    context = {'form': form, 'comment': comment}
    return render(request, "answer_comment.html", context)


@receiver(post_save, sender=AnswerComment)
def send_message_about_answer(sender, **kwargs):
    """Сигнал об оставленном ответе на комментарии"""

    print("Оставили ответ на комментарий")
    send_mail(
        'Оставили ответ на комментарий',
        'Вам оставили ответ на комментарий на БЛОГ ITECH http://127.0.0.1:8000/',
        'python.project2012@gmail.com',
        ['python.project2012@gmail.com'],
        fail_silently=False)
    print("Письмо отправлено с помощью сигнала - ответ на комментарий")


def category_post(request, category_id):
    categories = Category.objects.all()
    posts = Post.objects.filter(category_id=category_id)
    context = {'categories': categories, 'posts': posts}
    return render(request, "category_post.html", context)


def popular_posts(request):
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-views', '-likes')
    context = {'categories': categories, 'posts': posts}
    return render(request, "popular_posts.html", context)


###### REST API ##########

class CategoriesList(generics.ListAPIView):
    """вывод всех категорий на главной странице"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostsAllList(generics.ListAPIView):
    """список всех постов на главной странице"""
    queryset = Post.objects.all()
    serializer_class = PostsAllSerializer


class PostView(generics.RetrieveAPIView):
    """информация о посте без комментариев и лайков"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostsByCategoryList(generics.RetrieveAPIView):
    """все посты конкретной категории"""
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class PostDetailedView(generics.RetrieveAPIView):
    """пост с комментариями и ответами на комментарий"""
    queryset = Post.objects.all()
    serializer_class = PostDetailedSerializer


class PopularPostsList(generics.ListAPIView):
    """список популярных постов"""
    queryset = Post.objects.all().order_by('-views', '-likes')
    serializer_class = PostsAllSerializer


class SimilarRandomPosts(generics.RetrieveAPIView):
    """пост с 3-мя случайными похожими постами"""
    queryset = Post.objects.all()
    serializer_class = SimilarRandomPostsSerializer
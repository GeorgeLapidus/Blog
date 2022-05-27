from rest_framework import serializers

from .models import Category, Post, Comment, AnswerComment


class CategorySerializer(serializers.ModelSerializer):
    """сериализатор для вывода всех категорий"""

    class Meta:
        model = Category
        fields = ['title', ]


class PostsAllSerializer(serializers.ModelSerializer):
    """сериализатор для вывода всех постов"""

    class Meta:
        model = Post
        fields = ['title', 'briefdescription', 'created', 'image', 'views', ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    """сериализатор для вывода постов у конкретной категории"""
    post_set = PostsAllSerializer(many=True)

    class Meta:
        model = Category
        fields = ['post_set', ]


class PostSerializer(serializers.ModelSerializer):
    """сериализатор для конкретного поста"""

    class Meta:
        model = Post
        fields = ['title', 'description', 'created', 'image', 'views', ]


class AnswerCommentSerializer(serializers.ModelSerializer):
    """сериализатор для вывода ответов на комментарий"""

    class Meta:
        model = AnswerComment
        fields = ['date_created', 'text']


class CommentSerializer(serializers.ModelSerializer):
    """сериализатор для вывода комментрариев и ответов на комментарий(прошедших модерацию)"""
    answercomment_set = serializers.SerializerMethodField('get_answers')

    def get_answers(self, comment):
        qs = AnswerComment.objects.filter(is_publish=True, comment=comment)
        serializer = AnswerCommentSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Comment
        fields = ['date_created', 'text', 'answercomment_set']


class PostDetailedSerializer(serializers.ModelSerializer):
    """сериализатор для вывода конкретного поста с комментариями и ответами к нему(прошедших модерацию)"""
    comment_set = serializers.SerializerMethodField('get_comments')

    def get_comments(self, post):
        qs = Comment.objects.filter(is_publish=True, post=post)
        serializer = CommentSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Post
        fields = ['title', 'description', 'created', 'image', 'views', 'comment_set']

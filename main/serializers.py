from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    """Сериализатор для модели Категория"""
    title = serializers.CharField(max_length=200)


class PostSerializer(serializers.Serializer):
    """Сериализатор для модели Новоти"""
    category = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=1000)
    briefdescription = serializers.CharField(max_length=400)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    author = serializers.CharField(max_length=200)
    like = serializers.IntegerField()
    view = serializers.IntegerField()

class CommentSerializer(serializers.Serializer):
    """Сериализатор для модели Комментарии"""
    post = serializers.CharField(max_length=50)
    user = serializers.CharField(max_length=50)
    date_created = serializers.DateTimeField()
    text = serializers.CharField(max_length=1000)
    is_publish = serializers.BooleanField()
    likes = serializers.IntegerField()
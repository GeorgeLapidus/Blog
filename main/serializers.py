from rest_framework import serializers

from .models import Category, Post, Comment


class CategoryModelSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Категория через ModelSerializer"""

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


    class Meta:
        model = Category
        fields = '__all__'



class PostModelSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Новости через ModelSerializer"""

    category = CategoryModelSerializer()

    def create(self, validated_data):
        category_data = validated_data.pop("category")
        category = Category.objects.create(**category_data)
        # category, s = Category.objects.get_or_create(**category_data)
        post = Post.objects.create(category=category, **validated_data)
        return post



    class Meta:
        model = Post
        fields = '__all__'

class CommentModelSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Комментарии через ModelSerializer"""

    post = PostModelSerializer()

    class Meta:
        model = Comment
        fields = '__all__'



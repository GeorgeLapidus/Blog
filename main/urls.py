from django.urls import path

from main.views import start_page, post_detail, category_post, api_category, api_post, api_category_post, api_comments, \
    api_post_comments, answer_comment

app_name = "main"

urlpatterns = [
    path('', start_page, name="start_page"),
    path('post_detail/<int:id>', post_detail, name="post_detail"),
    path('category_post/<int:category_id>', category_post, name="category_post"),
    path('answer_comment/<int:id>', answer_comment, name="answer_comment"),

    path('api_category', api_category, name="api_category"),
    path('api_post', api_post, name="api_post"),
    path('api_category_post', api_category_post, name="api_category_post"),
    path('api_comments', api_comments, name="api_comments"),
    path('api_post_comments', api_post_comments, name="api_post_comments"),

]
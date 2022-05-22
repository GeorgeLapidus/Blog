from django.urls import path

from main.views import start_page, post_detail, category_post, \
    answer_comment, CategoryAll, PostAll, CommentAll, PostOne, CommentByPost, CategoryOne, CommentOne

app_name = "main"

urlpatterns = [
    path('', start_page, name="start_page"),
    path('post_detail/<int:id>', post_detail, name="post_detail"),
    path('category_post/<int:category_id>', category_post, name="category_post"),
    path('answer_comment/<int:id>', answer_comment, name="answer_comment"),

    path('api_category_all', CategoryAll.as_view(), name="api_category_all"),
    path('api_category_all/<int:id>', CategoryAll.as_view(), name="api_category_all"),
    path('api_category_one/<int:id>', CategoryOne.as_view(), name="api_category_one"),
    path('api_post_all', PostAll.as_view(), name="api_post_all"),
    path('api_post_one/<int:id>', PostOne.as_view(), name="api_post_one"),
    path('api_comment_by_post/<int:id>', CommentByPost.as_view(), name="api_comment_by_post"),
    path('api_comment_all', CommentAll.as_view(), name="api_comment_all"),
    path('api_comment_one/<int:id>', CommentOne.as_view(), name="api_comment_one"),


]
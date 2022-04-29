from django.urls import path

from main.views import start_page, post_detail, category_post

app_name = "main"

urlpatterns = [
    path('', start_page, name="start_page"),
    path('post_detail/<int:id>', post_detail, name="post_detail"),
    path('category_post/<int:category_id>', category_post, name="category_post"),
]
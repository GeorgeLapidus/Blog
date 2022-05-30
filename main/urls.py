from django.urls import path

from main.views import start_page, post_detail, category_post, answer_comment, \
    CategoriesList, PostsAllList, PostView, PostsByCategoryList, PostDetailedView, popular_posts, PopularPostsList, \
    SimilarRandomPosts

app_name = "main"

urlpatterns = [
    path('', start_page, name="start_page"),
    path('post_detail/<int:id>', post_detail, name="post_detail"),
    path('category_post/<int:category_id>', category_post, name="category_post"),
    path('popular_posts/', popular_posts, name="popular_posts"),
    path('answer_comment/<int:id>', answer_comment, name="answer_comment"),

    path('api/categories_list/', CategoriesList.as_view()),
    path('api/posts_list/', PostsAllList.as_view()),
    path('api/post/<int:pk>/', PostView.as_view()),
    path('api/category/<int:pk>/', PostsByCategoryList.as_view()),
    path('api/post_detailed/<int:pk>/', PostDetailedView.as_view()),
    path('api/popular_posts/', PopularPostsList.as_view()),
    path('api/similar_random_posts/<int:pk>/', SimilarRandomPosts.as_view()),
]

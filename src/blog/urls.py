from django.urls import path
from .views import index, article_detail

urlpatterns = [
    path('', index, name="blog-index"),
    path('article-<int:article_id>/', article_detail, name="blog-article"),
]
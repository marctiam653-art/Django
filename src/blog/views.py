from django.shortcuts import render, get_object_or_404
from .models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, "blog/index.html", context={"articles": articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "blog/article.html", context={"article": article})
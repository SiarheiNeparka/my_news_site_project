from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.
def article_list(request):
    articles = Article.published.all()

    return render(request, 'news/article/list.html', {'articles': articles})


def article_detail(request, year, month, day, article_slg):
    article = get_object_or_404(
        Article,
        status=Article.Status.PUBLISHED,
        slug=article_slg,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    return render(request, 'news/article/detail.html', {'article': article})

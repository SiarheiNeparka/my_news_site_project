from django.shortcuts import render, get_object_or_404
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView


# Create your views here.
class ArticleListView(ListView):
    '''Alternative article list view.'''

    queryset = Article.published.all()
    context_object_name = 'articles'
    paginate_by = 2
    template_name = 'news/article/list.html'


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

from django.shortcuts import render, get_object_or_404
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from mywebsite.settings import EMAIL_HOST_USER
from django.views.decorators.http import require_POST
from taggit.models import Tag


# Create your views here.
def article_list(request, tag_slug=None):
    article_list = Article.published.all()

    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        article_list = article_list.filter(tags__in=[tag])

    paginator = Paginator(article_list, 2)

    page_number = request.GET.get('page', 1)

    try:
        articles = paginator.page(page_number)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(
        request,
        'news/article/list.html',
        {'articles': articles, 'tag': tag},
    )


def article_detail(request, year, month, day, article_slg):
    article = get_object_or_404(
        Article,
        status=Article.Status.PUBLISHED,
        slug=article_slg,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    comments = article.comments.filter(active=True)

    form = CommentForm()

    return render(
        request,
        'news/article/detail.html',
        {'article': article, 'comments': comments, 'form': form},
    )


def article_share(request, year, month, day, article_slg):
    article = get_object_or_404(
        Article,
        status=Article.Status.PUBLISHED,
        slug=article_slg,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            article_url = request.build_absolute_uri(
                article.get_absolute_url(),
            )

            subject = f'{cd['name']} прислал Вам новость: {article.headline}'

            message = (
                f'Новость({article.headline}) доступна по ссылке {
                    article_url
                }'
            )

            if cd['comments']:
                message = (
                    message
                    + f'\n\n{cd['name']} оставил комментарий: \n{
                        cd['comments']
                    }'
                )

            send_mail(subject, message, EMAIL_HOST_USER, [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(
        request,
        'news/article/share.html',
        {'article': article, 'form': form, 'sent': sent},
    )


@require_POST
def article_comment(request, year, month, day, article_slg):
    article = get_object_or_404(
        Article,
        status=Article.Status.PUBLISHED,
        slug=article_slg,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    comment = None

    form = CommentForm(data=request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
    
    return render(
        request,
        'news/article/comment.html',
        {'article': article, 'form': form, 'comment': comment},
    )

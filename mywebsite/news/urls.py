from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path(
        'tag/<slug:tag_slug>/',
        views.article_list,
        name='article_list_by_tag',
    ),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:article_slg>/',
        views.article_detail,
        name='article_detail',
    ),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:article_slg>/share/',
        views.article_share,
        name='article_share',
    ),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:article_slg>/comment/',
        views.article_comment,
        name='article_comment',
    ),
]

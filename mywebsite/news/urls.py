from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:article_slg>/',
        views.article_detail,
        name='article_detail',
    ),
    path('<int:article_id>/share/', views.article_share, name='article_share'),
]

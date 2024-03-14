from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:id>/', views.article_detail, name='article_detail'),
]

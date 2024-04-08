from django.contrib import admin
from .models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['headline', 'slug', 'reporter', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'reporter']
    search_fields = ['headline', 'content']
    raw_id_fields = ['reporter']
    date_hierarchy = 'publish'
    ordering = ['publish', 'status']
    prepopulated_fields = {'slug': ('headline',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'article', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']

from django.contrib import admin
from .models import Article


# Register your models here.
# admin.site.register(Article)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["headline", "reporter", "publish"]
    list_filter = ["publish", "reporter"]
    search_fields = ["headline", "content"]
    raw_id_fields = ["reporter"]
    date_hierarchy = "publish"
    ordering = ["publish"]

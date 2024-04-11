from django.contrib.sitemaps import (
    _SupportsCount,
    _SupportsLen,
    _SupportsOrdered,
    Sitemap,
)
from .models import Article


class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self) -> _SupportsLen | _SupportsCount | _SupportsOrdered:
        return Article.publish.all()

    def lastmod(self, obj):
        return obj.updated

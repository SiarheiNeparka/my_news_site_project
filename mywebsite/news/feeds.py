from django.db.models.base import Model
import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Article


class LatestArticlesFeed(Feed):
    title = 'Новости'
    link = reverse_lazy('news:article_list')
    description = 'Самые свежие новости.'

    def items(self):
        return Article.published.all()[:3]

    def item_headline(self, item: Article):
        return item.headline

    def item_description(self, item: Article) -> str:
        return truncatewords_html(markdown.markdown(item.content), 30)

    def item_pubdate(self, item: Article):
        return item.publish

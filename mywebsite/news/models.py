from django.db import models
from django.utils import timezone


# Create your models here.
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name


class Article(models.Model):
    publish = models.DateField(default=timezone.now)
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-publish"]

    def __str__(self):
        return self.headline

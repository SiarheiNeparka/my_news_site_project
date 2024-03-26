# Generated by Django 4.1 on 2024-03-26 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('headline', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=250)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_articles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish'],
            },
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['-publish'], name='news_articl_publish_793b8b_idx'),
        ),
    ]

# Generated by Django 4.2.5 on 2024-03-19 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_news_content_en_news_content_ru_news_title_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='content_en',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ru',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ru',
        ),
    ]
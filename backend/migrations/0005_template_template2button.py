# Generated by Django 4.2.5 on 2024-03-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_remove_news_content_en_remove_news_content_ru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Ключь')),
                ('body_en', models.TextField(verbose_name='English')),
                ('body_ru', models.TextField(verbose_name='Русский')),
                ('body_uz', models.TextField(verbose_name='Uzbekcha')),
            ],
            options={
                'verbose_name': 'Шаблон',
                'verbose_name_plural': 'Шаблоны',
            },
        ),
        migrations.CreateModel(
            name='Template2Button',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Ключь')),
                ('body_en', models.TextField(verbose_name='English')),
                ('body_ru', models.TextField(verbose_name='Русский')),
                ('body_uz', models.TextField(verbose_name='Uzbekcha')),
            ],
            options={
                'verbose_name': 'Небольшой шаблон',
                'verbose_name_plural': 'Небольшие шаблоны',
            },
        ),
    ]

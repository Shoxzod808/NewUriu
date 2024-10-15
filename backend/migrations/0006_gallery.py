# Generated by Django 4.2.5 on 2024-03-20 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_template_template2button'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='gallery_photos/')),
                ('description_en', models.TextField(verbose_name='English')),
                ('description_ru', models.TextField(verbose_name='Русский')),
                ('description_uz', models.TextField(verbose_name='Uzbekcha')),
                ('date', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галерея',
            },
        ),
    ]

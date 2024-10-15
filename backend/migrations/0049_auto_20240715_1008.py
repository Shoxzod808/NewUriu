# Generated by Django 3.2.18 on 2024-07-15 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0048_auto_20240603_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='called',
            field=models.BooleanField(default=False, verbose_name='Не ответил'),
        ),
        migrations.AddField(
            model_name='contact',
            name='wait',
            field=models.BooleanField(default=False, verbose_name='Отказал'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Позвонил'),
        ),
    ]
# Generated by Django 5.0.3 on 2024-05-17 11:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0034_auto_20240426_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qabul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('passport', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('directions', models.CharField(max_length=100)),
                ('education_type', models.CharField(choices=[('full_time', 'Очное'), ('part_time', 'Заочное')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='text_en',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='text_ru',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='text_uz',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

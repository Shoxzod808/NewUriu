# Generated by Django 3.2.18 on 2024-04-26 06:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0033_alter_employee_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='body_en',
            field=ckeditor.fields.RichTextField(max_length=255, verbose_name='Текст(en)'),
        ),
        migrations.AlterField(
            model_name='document',
            name='body_ru',
            field=ckeditor.fields.RichTextField(max_length=255, verbose_name='Текст(ru)'),
        ),
        migrations.AlterField(
            model_name='document',
            name='body_uz',
            field=ckeditor.fields.RichTextField(max_length=255, verbose_name='Текст(uz)'),
        ),
    ]

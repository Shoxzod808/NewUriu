# Generated by Django 5.0.3 on 2024-04-16 10:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0025_rename_documente_filefordocuments_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='about_en',
            field=models.TextField(verbose_name='*Инфо(en)'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='about_ru',
            field=ckeditor.fields.RichTextField(verbose_name='*Инфо(ru)'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='about_uz',
            field=models.TextField(verbose_name='*Инфо(uz)'),
        ),
    ]

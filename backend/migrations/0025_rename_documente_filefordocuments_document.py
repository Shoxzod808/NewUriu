# Generated by Django 5.0.3 on 2024-04-09 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0024_document_filefordocuments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filefordocuments',
            old_name='documente',
            new_name='document',
        ),
    ]

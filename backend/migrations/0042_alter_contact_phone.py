# Generated by Django 5.0.3 on 2024-05-20 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0041_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]

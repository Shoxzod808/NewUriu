# Generated by Django 3.2.18 on 2024-05-24 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0043_auto_20240524_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='you_tube_video_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='education_type',
            field=models.CharField(choices=[('full_time', 'Kunduzgi'), ('part_time', 'Sirtqi')], default='part_time', max_length=20),
        ),
    ]

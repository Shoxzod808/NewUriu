# Generated by Django 4.2.5 on 2024-04-08 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_people_email_alter_people_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='*employee_photos/')),
                ('full_name_uz', models.CharField(max_length=255, verbose_name='*Имя(uz)')),
                ('full_name_en', models.CharField(max_length=255, verbose_name='*Имя(en)')),
                ('full_name_ru', models.CharField(max_length=255, verbose_name='*Имя(ru)')),
                ('proffesion_uz', models.CharField(max_length=255, verbose_name='*Профессия(uz)')),
                ('proffesion_en', models.CharField(max_length=255, verbose_name='*Профессия(en)')),
                ('proffesion_ru', models.CharField(max_length=255, verbose_name='*Профессия(ru)')),
                ('about_uz', models.TextField(max_length=255, verbose_name='*Инфо(ru)')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Почта')),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='Телеграм')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Телеграм')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Телеграм')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='SertificateForEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sertificates/')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SertificateForEmployee', to='backend.employee')),
            ],
        ),
        migrations.RemoveField(
            model_name='sertificateforpeople',
            name='news',
        ),
        migrations.DeleteModel(
            name='People',
        ),
        migrations.DeleteModel(
            name='SertificateForPeople',
        ),
    ]
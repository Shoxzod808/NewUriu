# Generated by Django 4.2.14 on 2024-09-16 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0050_auto_20240717_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='ac',
            field=models.BooleanField(default=False, verbose_name='Galdi'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='directions',
            field=models.CharField(choices=[("60110400 - Boshlang'ich ta'lim", "60110400 - Boshlang'ich ta'lim"), ('60220300 - Tarix', '60220300 - Tarix'), ("60230100 - Filoligiya va tillarni o'qitish(o'zbek tili)", "60230100 - Filoligiya va tillarni o'qitish(o'zbek tili)"), ("60230100 - Filoligiya va tillarni o'qitish(Ingliz tili)", "60230100 - Filoligiya va tillarni o'qitish(Ingliz tili)"), ("60230100 - Filoligiya va tillarni o'qitish(Rus tili)", "60230100 - Filoligiya va tillarni o'qitish(Rus tili)"), ('60410600 - Bank ishi', '60410600 - Bank ishi'), ('60410200 - Buxgalteriya hisobi', '60410200 - Buxgalteriya hisobi'), ('60610100 - Axborot tizimlari va texnologiyalar', '60610100 - Axborot tizimlari va texnologiyalar'), ('60410100 - Iqtisodiyot', '60410100 - Iqtisodiyot'), ('60310300 - Psixologiya', '60310300 - Psixologiya'), ('70220301 - Tarix', '70220301 -  Tarix'), ("70230101 - Lingvistika(o'zbek tili)", "70230101 - Lingvistika(o'zbek tili)"), ('70230101 - Lingvistika(ingliz tili)', '70230101 - Lingvistika(ingliz tili)'), ('70230101 - Lingvistika(rus tili)', '70230101 - Lingvistika(rus tili)')], default="Boshlang'ich ta'lim", max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=35, unique=True, verbose_name='Телефон'),
        ),
    ]
# Generated by Django 4.2 on 2023-12-14 11:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_module', '0007_products_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='favorit',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

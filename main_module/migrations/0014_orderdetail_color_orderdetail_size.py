# Generated by Django 4.2 on 2023-12-15 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0013_alter_products_color_alter_products_color2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='color',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='size',
            field=models.CharField(default='', max_length=100),
        ),
    ]

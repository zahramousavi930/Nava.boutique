# Generated by Django 4.2 on 2023-12-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0011_alter_products_color_alter_products_color2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

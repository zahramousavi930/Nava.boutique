# Generated by Django 4.2 on 2023-12-14 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0008_alter_products_favorit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_comments',
            name='rate',
        ),
    ]

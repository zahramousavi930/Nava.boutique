# Generated by Django 4.2 on 2023-12-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0017_remove_order_data_card_name_remove_order_data_cvs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='coount',
            field=models.IntegerField(default=1),
        ),
    ]

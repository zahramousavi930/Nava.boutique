# Generated by Django 4.2 on 2024-03-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0043_alter_orderdetail_final_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='order_number',
            field=models.IntegerField(default=0),
        ),
    ]

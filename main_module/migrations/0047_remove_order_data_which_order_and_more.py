# Generated by Django 4.2 on 2024-03-07 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0046_remove_orderdetail_coount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_data',
            name='which_order',
        ),
        migrations.RemoveField(
            model_name='order_data',
            name='which_user',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='order_data',
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
    ]

# Generated by Django 4.2 on 2023-12-21 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0025_remove_order_data_orderid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_data',
            name='orderid',
            field=models.ForeignKey(default=3412, on_delete=django.db.models.deletion.PROTECT, to='main_module.order'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2 on 2023-12-20 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0019_remove_order_data_street_address2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main_module.products'),
        ),
    ]

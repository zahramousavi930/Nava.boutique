# Generated by Django 4.2 on 2023-12-22 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0030_order_payment_time_alter_order_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_time',
            field=models.TimeField(blank=True, default='', null=True),
        ),
    ]

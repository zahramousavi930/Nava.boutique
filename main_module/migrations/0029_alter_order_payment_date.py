# Generated by Django 4.2 on 2023-12-22 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0028_remove_order_data_whichorder_order_data_which_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

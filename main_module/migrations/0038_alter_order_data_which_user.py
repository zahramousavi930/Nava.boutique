# Generated by Django 4.2 on 2023-12-22 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_module', '0037_remove_order_payment_time_alter_order_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_data',
            name='which_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

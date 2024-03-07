from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0041_remove_order_data_which_order_order_data_which_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='final_price',
            field=models.CharField(max_length=255, blank=True, null=True),  # Add max_length parameter here
        ),
    ]

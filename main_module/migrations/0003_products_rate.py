# Generated by Django 4.2 on 2023-12-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0002_contact_contact_with_us_news_teller_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='rate',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=234, max_length=1000),
            preserve_default=False,
        ),
    ]

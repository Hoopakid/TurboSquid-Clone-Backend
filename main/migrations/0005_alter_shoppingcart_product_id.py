# Generated by Django 4.2.7 on 2023-11-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_shoppingcart_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='product_id',
            field=models.FloatField(),
        ),
    ]

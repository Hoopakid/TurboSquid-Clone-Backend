# Generated by Django 4.2.7 on 2023-11-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_shoppingcart_product_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='product_id',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='user',
            field=models.CharField(max_length=12),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_product_long_description_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.TextField(default='7', verbose_name='Sizes (seperated by comma (,):'),
            preserve_default=False,
        ),
    ]
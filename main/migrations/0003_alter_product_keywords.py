# Generated by Django 4.2.7 on 2023-12-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_auximage_product_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='keywords',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

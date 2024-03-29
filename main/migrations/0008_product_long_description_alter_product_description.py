# Generated by Django 4.2.7 on 2023-12-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='long_description',
            field=models.TextField(default='description', verbose_name='Detailed Description (max: 80 words)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Short Description (max: 30 words)'),
        ),
    ]

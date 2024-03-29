# Generated by Django 4.2.7 on 2023-12-15 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_vogueusers_vogueuser'),
        ('main', '0004_remove_product_auximage_product_auximage1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.vogueuser')),
            ],
        ),
    ]

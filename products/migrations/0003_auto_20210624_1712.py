# Generated by Django 2.2.12 on 2021-06-24 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210624_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
    ]
# Generated by Django 5.0.6 on 2024-05-20 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_product_demand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demand',
            old_name='Category',
            new_name='category',
        ),
    ]

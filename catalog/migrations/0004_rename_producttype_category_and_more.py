# Generated by Django 5.0.2 on 2024-02-20 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_product_options_rename_title_product_name"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ProductType",
            new_name="Category",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="format",
            new_name="category",
        ),
    ]

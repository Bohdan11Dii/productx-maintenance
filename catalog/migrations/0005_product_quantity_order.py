# Generated by Django 5.0.2 on 2024-02-27 20:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_rename_producttype_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(default="", max_length=100)),
                ("last_name", models.CharField(default="", max_length=100)),
                (
                    "phone",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MaxValueValidator(10)],
                    ),
                ),
                ("department", models.TextField(default="Your department")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                    ),
                ),
            ],
            options={
                "ordering": ("product",),
            },
        ),
    ]

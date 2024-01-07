# Generated by Django 4.2.7 on 2024-01-07 06:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sample", "0004_employee"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trip",
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
                ("Days", models.CharField(max_length=255)),
                ("Origin", models.CharField(max_length=255)),
                ("Destination", models.CharField(max_length=255)),
            ],
        ),
    ]

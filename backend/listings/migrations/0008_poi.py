# Generated by Django 4.1.3 on 2022-12-05 18:55

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0007_remove_listing_location_listing_latitude_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Poi",
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
                ("name", models.CharField(blank=True, max_length=120, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("University", "University"),
                            ("Hospital", "Hospital"),
                            ("Stadium", "Stadium"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "location",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True, null=True, srid=4326
                    ),
                ),
            ],
        ),
    ]

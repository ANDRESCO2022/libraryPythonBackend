# Generated by Django 3.2 on 2022-08-02 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BookCopy",
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
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

# Generated by Django 3.2 on 2022-08-06 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_userlibrary_adress"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userlibrary",
            name="adress",
        ),
    ]

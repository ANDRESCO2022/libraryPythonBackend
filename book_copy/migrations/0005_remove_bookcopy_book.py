# Generated by Django 3.2 on 2022-08-03 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book_copy", "0004_remove_bookcopy_shelf"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bookcopy",
            name="book",
        ),
    ]

# Generated by Django 3.2 on 2022-08-03 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book_copy", "0003_alter_bookcopy_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bookcopy",
            name="shelf",
        ),
    ]

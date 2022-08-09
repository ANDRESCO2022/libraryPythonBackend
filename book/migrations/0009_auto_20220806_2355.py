# Generated by Django 3.2 on 2022-08-07 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0008_remove_book_book_copy"),
    ]

    operations = [
        migrations.RenameField(
            model_name="author",
            old_name="first_name",
            new_name="full_name",
        ),
        migrations.RemoveField(
            model_name="author",
            name="date_birth",
        ),
        migrations.RemoveField(
            model_name="author",
            name="last_name",
        ),
        migrations.AddField(
            model_name="author",
            name="nationality",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="book",
            name="status",
            field=models.CharField(
                choices=[("avalible", "avalible"), ("reserved", "reserved")],
                default="avalible",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="status",
            field=models.CharField(
                choices=[("active", "active"), ("inactive", "inactive")],
                default="active",
                max_length=15,
            ),
        ),
    ]

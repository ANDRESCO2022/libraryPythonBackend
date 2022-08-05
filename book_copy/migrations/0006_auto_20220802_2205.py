# Generated by Django 3.2 on 2022-08-03 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_copy", "0005_remove_bookcopy_book"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookcopy",
            options={},
        ),
        migrations.RemoveField(
            model_name="bookcopy",
            name="due_back",
        ),
        migrations.RemoveField(
            model_name="bookcopy",
            name="status",
        ),
        migrations.AddField(
            model_name="bookcopy",
            name="name",
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="bookcopy",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]

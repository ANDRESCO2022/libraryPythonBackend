# Generated by Django 3.2 on 2022-08-07 05:58

import isbn_field.fields
import isbn_field.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0010_book_isbn"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="dirty_isbn",
            field=isbn_field.fields.ISBNField(
                clean_isbn=False,
                default=1,
                max_length=28,
                validators=[isbn_field.validators.ISBNValidator],
                verbose_name="ISBN",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="book",
            name="isbn",
            field=isbn_field.fields.ISBNField(
                max_length=28,
                validators=[isbn_field.validators.ISBNValidator],
                verbose_name="ISBN",
            ),
        ),
    ]

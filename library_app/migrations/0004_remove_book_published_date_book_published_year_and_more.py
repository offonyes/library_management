# Generated by Django 5.0.6 on 2024-05-30 14:36

import django.core.validators
import library_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_alter_book_options_book_image_link_alter_book_genres_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_date',
        ),
        migrations.AddField(
            model_name='book',
            name='published_year',
            field=models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(1800), library_app.models.max_value_current_year], verbose_name='Published Year'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='image_link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Image Link'),
        ),
    ]

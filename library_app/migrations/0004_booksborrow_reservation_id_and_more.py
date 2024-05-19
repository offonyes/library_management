# Generated by Django 5.0.6 on 2024-05-18 18:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_alter_book_options_alter_book_genres_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksborrow',
            name='reservation_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrows', to='library_app.bookreservation', verbose_name='Reservation Id'),
        ),
        migrations.AlterField(
            model_name='bookreservation',
            name='reservation_status',
            field=models.CharField(choices=[('reserved', 'Reserved a book'), ('reservation_expired', 'Reservation expired'), ('reservation_canceled', 'Reservation canceled'), ('out_of_stock', 'Out of stock, added to wishlist'), ('picked_up', 'Picked up the book')], default='reserved', max_length=50, verbose_name='Status'),
        ),
    ]
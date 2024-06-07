# Generated by Django 5.0.6 on 2024-05-30 16:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='personal_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='Personal Number'),
        ),
    ]
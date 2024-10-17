# Generated by Django 5.0.6 on 2024-05-24 07:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artapp', '0002_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='mobnum',
            field=models.CharField(help_text='Enter a valid mobile number', max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '9999999999'. Up to 11 digits allowed.", regex='^\\d{10,11}$')], verbose_name='Mobile Number'),
        ),
    ]

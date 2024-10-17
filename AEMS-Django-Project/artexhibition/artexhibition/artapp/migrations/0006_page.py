# Generated by Django 5.0.6 on 2024-05-27 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artapp', '0005_artproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagetitle', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('aboutus', models.TextField()),
                ('email', models.EmailField(max_length=200)),
                ('mobilenumber', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
# Generated by Django 5.0.6 on 2024-05-27 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artapp', '0003_alter_artist_email_alter_artist_mobnum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artmedium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artmedium', models.CharField(max_length=250)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Arttype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arttype', models.CharField(max_length=250)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

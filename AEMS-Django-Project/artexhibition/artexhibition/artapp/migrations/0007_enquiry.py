# Generated by Django 5.0.6 on 2024-05-29 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artapp', '0006_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquirynumber', models.IntegerField(default=0, unique=True)),
                ('fullname', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=200)),
                ('prod_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artproducts', to='artapp.artproducts')),
            ],
        ),
    ]
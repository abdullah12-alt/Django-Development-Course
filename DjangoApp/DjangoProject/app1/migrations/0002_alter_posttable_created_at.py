# Generated by Django 5.0.6 on 2024-05-24 04:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttable',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 5, 24, 4, 41, 53, 698864, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-25 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='post_img/'),
        ),
    ]

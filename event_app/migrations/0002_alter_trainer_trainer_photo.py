# Generated by Django 3.2 on 2021-05-06 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='trainer_photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/trainer_photos/'),
        ),
    ]

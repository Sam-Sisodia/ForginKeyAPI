# Generated by Django 4.1 on 2022-09-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='state_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]

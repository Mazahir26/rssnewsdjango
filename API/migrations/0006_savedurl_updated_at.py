# Generated by Django 3.2.5 on 2021-07-25 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_auto_20210725_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedurl',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-25 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_auto_20210703_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='Category',
            field=models.CharField(default='General', max_length=30),
        ),
        migrations.AlterField(
            model_name='feed',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

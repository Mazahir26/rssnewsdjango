# Generated by Django 3.2.5 on 2021-07-03 06:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('feed', models.URLField(unique=True)),
                ('Users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

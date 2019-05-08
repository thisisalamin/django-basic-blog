# Generated by Django 2.2.1 on 2019-05-08 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('descriptions', models.TextField()),
                ('publish', models.DateTimeField(default=datetime.datetime(2019, 5, 8, 12, 6, 36, 741604), verbose_name='published')),
            ],
        ),
    ]

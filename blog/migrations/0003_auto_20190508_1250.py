# Generated by Django 2.2.1 on 2019-05-08 06:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190508_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 8, 12, 50, 5, 513533), verbose_name='published'),
        ),
    ]

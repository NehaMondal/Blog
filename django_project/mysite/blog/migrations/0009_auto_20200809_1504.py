# Generated by Django 2.2.4 on 2020-08-09 09:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200809_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 9, 34, 34, 898392, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 9, 34, 34, 898392, tzinfo=utc)),
        ),
    ]

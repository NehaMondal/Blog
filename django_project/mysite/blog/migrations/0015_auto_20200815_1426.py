# Generated by Django 2.2.4 on 2020-08-15 08:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200815_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 15, 8, 56, 53, 564321, tzinfo=utc)),
        ),
    ]

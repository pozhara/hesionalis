# Generated by Django 3.2.19 on 2023-07-15 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20230715_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_at',
            field=models.DateTimeField(blank='true', default=datetime.datetime(2023, 7, 15, 14, 45, 41, 115861)),
        ),
    ]

# Generated by Django 3.2.19 on 2023-07-16 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_appointment_appointment_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_at',
        ),
    ]

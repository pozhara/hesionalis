# Generated by Django 3.2.19 on 2023-07-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_appointment_appointment_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_at',
            field=models.DateTimeField(),
        ),
    ]

# Generated by Django 3.2.19 on 2023-06-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='bio',
        ),
        migrations.AddField(
            model_name='artist',
            name='skills',
            field=models.CharField(blank=True, choices=[('Traditional', 'Traditional'), ('Neo Traditional', 'Neo Traditional'), ('Fine Line', 'Fine Line'), ('Tribal', 'Tribal'), ('Watercolor', 'Watercolor'), ('Blackwork', 'Blackwork'), ('Realism', 'Realism'), ('Japanese', 'Japanese'), ('Patchwork', 'Patchwork'), ('Ignorant', 'Ignorant'), ('Portrait', 'Portrait'), ('Animal', 'Animal'), ('Floral', 'Floral')], max_length=30, null=True),
        ),
    ]

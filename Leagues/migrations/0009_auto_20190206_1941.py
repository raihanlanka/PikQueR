# Generated by Django 2.1.2 on 2019-02-07 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Leagues', '0008_dailyleague'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamleague',
            name='categoryname',
        ),
        migrations.RemoveField(
            model_name='teamleague',
            name='members',
        ),
        migrations.DeleteModel(
            name='TeamLeague',
        ),
    ]

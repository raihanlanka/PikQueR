# Generated by Django 2.1.2 on 2018-12-10 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20181210_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

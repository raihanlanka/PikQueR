# Generated by Django 2.1.2 on 2018-12-10 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 12, 10, 10, 16, 2, 292981)),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 12, 10, 10, 16, 2, 292981)),
        ),
    ]

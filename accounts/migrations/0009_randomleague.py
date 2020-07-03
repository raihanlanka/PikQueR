# Generated by Django 2.1.2 on 2018-11-12 21:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0008_profile_piccredits'),
    ]

    operations = [
        migrations.CreateModel(
            name='randomleague',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaguename', models.CharField(max_length=200, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('members', models.ManyToManyField(blank=True, related_name='randommembers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

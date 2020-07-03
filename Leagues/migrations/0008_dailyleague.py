# Generated by Django 2.1.2 on 2018-12-31 18:01

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Leagues', '0007_freeleaguechat'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyLeague',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=200, null=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('members', models.ManyToManyField(blank=True, related_name='DailyLeagueMembers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

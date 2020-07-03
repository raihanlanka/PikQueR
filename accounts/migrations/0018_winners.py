# Generated by Django 2.1.2 on 2018-11-18 18:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0017_auto_20181114_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='winners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winnerleaguename', models.ManyToManyField(blank=True, related_name='winnerleaguename', to='accounts.league')),
                ('winningmembers', models.ManyToManyField(blank=True, related_name='winningmembers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

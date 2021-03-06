# Generated by Django 2.1.2 on 2018-12-13 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_auto_20181210_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dailyleaguescore',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='profile',
            name='leaguescore',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='profile',
            name='piccredits',
            field=models.DecimalField(decimal_places=1, default=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profilescore',
            field=models.DecimalField(decimal_places=3, default=10, max_digits=8),
        ),
    ]

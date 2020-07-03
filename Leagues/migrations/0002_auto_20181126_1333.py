# Generated by Django 2.1.2 on 2018-11-26 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leagues', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freeleague',
            name='leaguename',
        ),
        migrations.RemoveField(
            model_name='hotleague',
            name='leaguename',
        ),
        migrations.RemoveField(
            model_name='megaleague',
            name='leaguename',
        ),
        migrations.RemoveField(
            model_name='randomleague',
            name='categoryname',
        ),
        migrations.RemoveField(
            model_name='randomleague',
            name='leaguename',
        ),
        migrations.AlterField(
            model_name='freeleague',
            name='categoryname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hotleague',
            name='categoryname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='megaleague',
            name='categoryname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

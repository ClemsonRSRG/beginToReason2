# Generated by Django 3.2.4 on 2021-06-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_analysis', '0007_datalog_is_alternate'),
    ]

    operations = [
        migrations.AddField(
            model_name='datalog',
            name='time_took',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='datalog',
            name='vcs',
            field=models.TextField(default='null'),
        ),
    ]

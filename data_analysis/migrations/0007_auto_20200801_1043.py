# Generated by Django 3.0.8 on 2020-08-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_analysis', '0006_auto_20200801_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datalog',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

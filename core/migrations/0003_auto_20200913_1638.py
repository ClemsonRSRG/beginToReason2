# Generated by Django 3.1.1 on 2020-09-13 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200913_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='lesson_code',
            field=models.TextField(max_length=750),
        ),
    ]
# Generated by Django 3.2.5 on 2021-08-11 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20210604_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='correctExpression',
            field=models.TextField(default='/*expression*/'),
        ),
    ]
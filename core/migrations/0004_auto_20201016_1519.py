# Generated by Django 3.1.2 on 2020-10-16 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201016_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='ALG',
            new_name='algebra',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='INIT',
            new_name='not_using_initial_value',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='NUM',
            new_name='self_reference',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='SELF',
            new_name='simplify',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='SIM',
            new_name='use_of_concrete_values',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='VAR',
            new_name='variable',
        ),
    ]

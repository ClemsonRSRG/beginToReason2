# Generated by Django 3.2.4 on 2021-10-04 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_lesson_multi_confirms'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='sortable_lines',
            field=models.TextField(default=''),
        ),
    ]
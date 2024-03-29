# Generated by Django 3.2.9 on 2021-11-23 05:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
        ('educator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_alternate', models.BooleanField()),
                ('status', models.CharField(max_length=50)),
                ('code', models.TextField(default='null')),
                ('explanation', models.TextField()),
                ('face', models.TextField(default='null')),
                ('original_code', models.TextField(default='null')),
                ('vcs', models.TextField(default='null')),
                ('time_took', models.FloatField(null=True)),
                ('assignment_key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='educator.assignment')),
                ('lesson_key', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.lesson')),
                ('lesson_set_key', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.lessonset')),
                ('user_key', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

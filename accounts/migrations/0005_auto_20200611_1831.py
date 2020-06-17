# Generated by Django 3.0.7 on 2020-06-11 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200611_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='user_gender',
            field=models.CharField(choices=[('American Indian or Alaska Native', 'American Indian or Alaska Native'), ('Asian', 'Asian'), ('Black or African American', 'Black or African American'), ('Hispanic or Latino', 'Hispanic or Latino'), ('Native Hawaiian or Other Pacific Islander', 'Native Hawaiian or Other Pacific Islander'), ('White', 'White'), ('Prefer Not To Answer', 'Prefer Not To Answer')], default='Prefer Not To Answer', max_length=50),
        ),
    ]
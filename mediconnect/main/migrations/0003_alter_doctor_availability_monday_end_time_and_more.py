# Generated by Django 4.2.1 on 2023-05-06 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_generaldiagnosticquestions_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='availability_monday_end_time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 6, 21, 36, 54, 468155, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='availability_tuesday_end_time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 6, 21, 36, 54, 468155, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='availability_wednesday_end_time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 6, 21, 36, 54, 468155, tzinfo=datetime.timezone.utc)),
        ),
    ]

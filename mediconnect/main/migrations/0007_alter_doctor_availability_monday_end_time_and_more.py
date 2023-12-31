# Generated by Django 4.2.1 on 2023-05-07 00:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_remove_feedback_doctor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='availability_monday_end_time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 7, 4, 0, 46, 747267, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='availability_tuesday_end_time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 7, 4, 0, 46, 747267, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='availability_wednesday_end_time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 7, 4, 0, 46, 747267, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

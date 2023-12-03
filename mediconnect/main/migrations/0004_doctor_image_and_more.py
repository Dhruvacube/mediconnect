# Generated by Django 4.2.1 on 2023-05-06 18:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('main', '0003_alter_doctor_availability_monday_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_image', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='availability_monday_end_time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 6, 22, 23, 17, 225906, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='availability_tuesday_end_time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 6, 22, 23, 17, 226905, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='availability_wednesday_end_time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 6, 22, 23, 17, 226905, tzinfo=datetime.timezone.utc)),
        ),
    ]

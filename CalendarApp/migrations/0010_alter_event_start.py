# Generated by Django 4.0 on 2021-12-11 19:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalendarApp', '0009_alter_event_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 11, 20, 49, 16, 722221), null=True, verbose_name='Data Inicio'),
        ),
    ]
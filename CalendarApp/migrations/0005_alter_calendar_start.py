# Generated by Django 4.0 on 2021-12-11 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalendarApp', '0004_alter_calendar_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='start',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Data Inicio'),
        ),
    ]
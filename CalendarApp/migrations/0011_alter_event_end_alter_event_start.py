# Generated by Django 4.0 on 2021-12-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalendarApp', '0010_alter_event_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.CharField(blank=True, default='2021-12-11T22:30:00', max_length=20, null=True, verbose_name='Data Final'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.CharField(blank=True, default='2021-12-11T22:30:00', max_length=20, null=True, verbose_name='Data Inicio'),
        ),
    ]
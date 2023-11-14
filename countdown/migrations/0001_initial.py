# Generated by Django 4.2.6 on 2023-10-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OneTimeEvent',
            fields=[
                ('event_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_time', models.DateTimeField(verbose_name='event time')),
            ],
        ),
        migrations.CreateModel(
            name='RepeatableEvent',
            fields=[
                ('event_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('repeat_event_each_days', models.IntegerField()),
                ('event_day_of_month', models.CharField(max_length=3)),
                ('event_day_of_week', models.CharField(max_length=20)),
                ('event_time', models.TimeField()),
            ],
        ),
    ]

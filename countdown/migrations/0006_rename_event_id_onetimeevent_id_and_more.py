# Generated by Django 4.2.6 on 2023-11-09 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countdown', '0005_remove_repeatableevent_repeat_event_each_days'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onetimeevent',
            old_name='event_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='repeatableevent',
            old_name='event_id',
            new_name='id',
        ),
        migrations.AddField(
            model_name='onetimeevent',
            name='user',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='repeatableevent',
            name='user',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

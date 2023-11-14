from django.db import models


class OneTimeEvent(models.Model):
    event_name = models.CharField(max_length=200)
    event_time = models.DateTimeField("event time")
    user = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.event_name


class RepeatableEvent(models.Model):
    event_name = models.CharField(max_length=200)
    event_day_of_month = models.CharField(max_length=3, blank=True)
    event_day_of_week = models.CharField(max_length=20,
                                         choices=(('1', 'Monday'), ('2', 'Tuesday'),
                                                  ('3', 'Wednesday'), ('4', 'Thursday'),
                                                  ('5', 'Friday'), ('6', 'Saturday'),
                                                  ('0', 'Sunday'),), blank=True)
    event_time = models.TimeField()
    user = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.event_name

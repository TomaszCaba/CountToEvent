from django.contrib import admin
from .models import OneTimeEvent, RepeatableEvent





admin.site.register(OneTimeEvent)
admin.site.register(RepeatableEvent)

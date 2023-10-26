# from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import OneTimeEvent, RepeatableEvent


class IndexView(generic.ListView):
    template_name = "countdown/index.html"
    context_object_name = "all_countdowns"

    def get_queryset(self):
        return {'one_time_events': OneTimeEvent.objects.all(), 'repeatable_events': RepeatableEvent.objects.all()}


def index(request):
    context = {'main': "countdown/index.html", 'one_time_events': OneTimeEvent.objects.all(), 'repeatable_events': RepeatableEvent.objects.all()}
    return render(request, "countdown/base.html", context)


def one_time_detail(request, one_time_id):
    countdown = get_object_or_404(OneTimeEvent, pk=one_time_id)
    context = {"countdown": countdown, "main": "countdown/OneTimeCountdown.html",
               "title": f"Counting to {countdown.event_name}",
               "css": ["countdown/style/onetimecountdown_style.css",]}
    return render(request, "countdown/base.html", context)


def repeatable_detail(request, repeatable_id):
    countdown = get_object_or_404(RepeatableEvent, pk=repeatable_id)
    context = {"repeatableevent": countdown, "main": "countdown/RepeatableCountdown.html",
               "title": f"Counting to {countdown.event_name}",
               "css": ["countdown/style/repeatablecountdown_style.css", ]}
    return render(request, "countdown/base.html", context)

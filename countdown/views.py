from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import OneTimeEvent, RepeatableEvent
from django.contrib.auth.decorators import login_required
from itertools import chain


def index(request):
    if request.user.is_authenticated:
        context = {'main': "countdown/index.html",
                   'one_time_events': chain(OneTimeEvent.objects.filter(user=request.user.username),
                                            OneTimeEvent.objects.filter(user="")),
                   'repeatable_events': chain(RepeatableEvent.objects.filter(user=""),
                                              RepeatableEvent.objects.filter(user=request.user.username))}
    else:
        context = {'main': "countdown/index.html",
                   'one_time_events': OneTimeEvent.objects.filter(user=""),
                   'repeatable_events': RepeatableEvent.objects.filter(user="")}
    return render(request, "countdown/index.html", context)


def one_time_detail(request, one_time_id):
    countdown = get_object_or_404(OneTimeEvent, pk=one_time_id)
    context = {"countdown": countdown, "main": "countdown/one_time_countdown.html",
               "title": f"Counting to {countdown.event_name}",
               "css": ["countdown/style/onetimecountdown_style.css", ]}
    if countdown.user == request.user.username or countdown.user == "":
        return render(request, "countdown/one_time_countdown.html", context)
    return HttpResponseRedirect(reverse('countdown:index'))


def repeatable_detail(request, repeatable_id):
    countdown = get_object_or_404(RepeatableEvent, pk=repeatable_id)
    context = {"repeatableevent": countdown, "main": "countdown/repeatable_countdown.html",
               "title": f"Counting to {countdown.event_name}",
               "css": ["countdown/style/repeatablecountdown_style.css", ]}

    if countdown.user == request.user.username or countdown.user == "":
        return render(request, "countdown/repeatable_countdown.html", context)
    return HttpResponseRedirect(reverse('countdown:index'))


@login_required
def profile(request):
    return render(request, 'countdown/profile.html',
                  context={"repeatable_events": RepeatableEvent.objects.filter(user=request.user.username),
                           "one_time_events": OneTimeEvent.objects.filter(user=request.user.username),
                           "css": ["/countdown/style/profile_style.css"]})


@login_required
def update_confirm(request, counter_type, event_id):
    if counter_type == "repeatable":
        countdown = get_object_or_404(RepeatableEvent, pk=event_id)
        return render(request, 'countdown/update_counter.html', {"countdown": countdown,
                                                                 "event_type": counter_type,
                                                                 "event_time": str(countdown.event_time)[:5]})
    countdown = get_object_or_404(OneTimeEvent, pk=event_id)
    return render(request, 'countdown/update_counter.html', {"countdown": countdown,
                                                             "event_type": counter_type,
                                                             "event_date": str(countdown.event_time).split(" ")[0],
                                                             "event_time": str(countdown.event_time).split(" ")[1][:5]})


@login_required
def destroy_countdown(request, counter_type, event_id):
    if counter_type == "repeatable":
        countdown = get_object_or_404(RepeatableEvent, pk=event_id)
    else:
        countdown = get_object_or_404(OneTimeEvent, pk=event_id)
    if countdown.user == request.user.username:
        countdown.delete()
        return HttpResponseRedirect(reverse('countdown:profile'))
    return HttpResponseRedirect(reverse('countdown:index'))


@login_required
def add_confirm(request):
    return render(request, 'countdown/create_counter.html')


@login_required
def add_countdown(request):
    if request.POST['counter_type'] == 'repeatable':
        new_countdown = RepeatableEvent()
        new_countdown.event_name = request.POST['event_name']
        new_countdown.event_day_of_month = request.POST['event_day_of_month']
        new_countdown.event_day_of_week = request.POST['event_day_of_week']
        new_countdown.event_time = request.POST['event_time']
        new_countdown.user = request.user.username
        new_countdown.save()
    elif request.POST['counter_type'] == 'onetime':
        new_countdown = OneTimeEvent()
        new_countdown.event_name = request.POST['event_name']
        new_countdown.event_time = request.POST['event_date'] + " " + request.POST['event_time']
        new_countdown.user = request.user.username
        new_countdown.save()
    return HttpResponseRedirect(reverse('countdown:index'))


@login_required
def update_countdown(request, counter_type, event_id):
    if counter_type == "repeatable":
        countdown = get_object_or_404(RepeatableEvent, pk=event_id)
        countdown.event_day_of_week = request.POST['event_day_of_week']
        countdown.event_day_of_month = request.POST['event_day_of_month']
        countdown.event_name = request.POST['event_time']
    else:
        countdown = get_object_or_404(OneTimeEvent, pk=event_id)
        countdown.event_time = request.POST['event_date'] + " " + request.POST['event_time']
    countdown.event_name = request.POST['event_name']
    if countdown.user == request.user.username:
        countdown.save()
        return HttpResponseRedirect(reverse('countdown:profile'))
    else:
        return HttpResponseRedirect(reverse('countdown:index'))

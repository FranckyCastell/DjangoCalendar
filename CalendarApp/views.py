from django.shortcuts import render
from CalendarApp.models import Event

# Create your views here.


def calendar(request):

    events = Event.objects.all()

    context = {'events': events}
    return render(request, 'CalendarApp/calendar.html', context)

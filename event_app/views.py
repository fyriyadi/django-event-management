from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Event, Trainer, Participant
#for authorized page (is_staff)
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def eventPage(request):
    events = Event.objects.all()
    trainers = Trainer.objects.all()
    context = {'events' : events, 'trainers' : trainers}
    
    return render(request, 'event_app/event_home.html',context)

def eventDetail(request,id):
    event = Event.objects.get(id=id)
    facilities = event.event_facilities.all()
    trainers = event.event_trainer.all()

    return render(request, 'event_app/event_detail.html', {'event' : event, 'facilities' : facilities, 'trainers':trainers,})


def eventRegister(request,id):
    reg_event, created = Participant.objects.get_or_create(event = Event.objects.get(id=id), user = request.user)
    if(created):
        messages.success(request, 'Successfully registered')
    else:
        messages.error(request, 'Already registered')
    
    return redirect ('eventdetail',id)


@user_passes_test(lambda user: user.is_staff)
def eventAttendance(request):
    participants = Participant.objects.all()

    return render(request, 'event_app/admin/participant.html', {'participants':participants})
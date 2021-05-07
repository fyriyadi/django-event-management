from django.shortcuts import render
from .models import Event, Trainer

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
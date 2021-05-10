from django.contrib import admin
from .models import *
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    filter_horizontal = ('event_facilities',)
class ParticipantAdmin(admin.ModelAdmin):
    fields = ('event','user','payment_status','attendance_status',)
    list_display = ['event','user','payment_status','attendance_status']
    list_filter = [
        'event',
        'user',
        'payment_status',
        'attendance_status',
    ]
    #search fields refer to related field name
    search_fields = ['event__event_name','user__username']

admin.site.register(Event, EventAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register([
    Trainer,
    Facility,
    
])

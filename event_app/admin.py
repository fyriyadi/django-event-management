from django.contrib import admin
from .models import *
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    filter_horizontal = ('event_facilities',)

admin.site.register(Event, EventAdmin)
admin.site.register(Facility)
admin.site.register(Trainer)
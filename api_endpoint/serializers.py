from rest_framework import serializers
from event_app.models import Participant, Event

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = (
            'event',
            'user',
            'payment_status',
            'attendance_status',
        )
        


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'event_name',
            'event_category',
            'event_audience',
            'event_venue',
            'event_start_time',
            'event_finish_time',
            'ticket_price',
            'ticket_available',
            'event_summary',
            'event_facilities',
            'event_trainer',
        )
        depth = 1

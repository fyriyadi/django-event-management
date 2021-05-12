from rest_framework import serializers
from event_app.models import Participant

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = (
            'event',
            'user',
            'payment_status',
            'attendance_status',
        )
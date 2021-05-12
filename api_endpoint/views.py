from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import ParticipantSerializer
from event_app.models import Participant

class ParticipantView(APIView):
    permission_classes =(IsAuthenticated,)
    
    def get(self,request,*args,**kwargs):
        participants = Participant.objects.all()
        serializer = ParticipantSerializer(participants, many=True)
        return Response(serializer.data)


    
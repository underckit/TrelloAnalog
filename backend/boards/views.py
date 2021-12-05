from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TrelloSerializer
from .models import Trello

# Create your views here.

class TrelloView(viewsets.ModelViewSet):
    serializer_class = TrelloSerializer
    queryset = Trello.objects.all()
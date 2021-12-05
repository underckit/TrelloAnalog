from rest_framework import serializers
from .models import Trello

class TrelloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trello
        fields = ('id', 'title', 'description', 'completed')
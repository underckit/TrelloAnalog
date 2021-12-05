from django.contrib import admin
from .models import Trello

class TrelloAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

admin.site.register(Trello, TrelloAdmin)
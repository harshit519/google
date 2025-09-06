from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('summary', 'start_time', 'end_time')
    list_filter = ('start_time', 'end_time')
    search_fields = ('summary',)
    ordering = ('start_time',)

from django.contrib import admin
from .models import Event, GoogleCredential

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('summary', 'start_time', 'end_time')
    list_filter = ('start_time', 'end_time')
    search_fields = ('summary',)
    ordering = ('start_time',)

@admin.register(GoogleCredential)
class GoogleCredentialAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'is_active', 'updated_at')
    list_filter = ('is_active',)

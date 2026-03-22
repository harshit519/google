from django.db import models
# calendar_integration/models.py
from django.db import models

class Event(models.Model):
    summary = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

# Create your models here.

class GoogleCredential(models.Model):
    client_id = models.CharField(max_length=255, help_text="Your Google App Client ID")
    client_secret = models.CharField(max_length=255, help_text="Your Google App Client Secret")
    access_token = models.TextField(blank=True, null=True, help_text="Current Access Token (can be left blank)")
    refresh_token = models.TextField(blank=True, null=True, help_text="Current Refresh Token (can be left blank)")
    is_active = models.BooleanField(default=True, help_text="Use these credentials as active")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Google Credentials (Active: {self.is_active})"

    class Meta:
        verbose_name = "Google Credential"
        verbose_name_plural = "Google Credentials"

from django.db import models
# calendar_integration/models.py
from django.db import models

class Event(models.Model):
    summary = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

# Create your models here.

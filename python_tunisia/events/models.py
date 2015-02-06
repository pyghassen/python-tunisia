"""
Events model module.
"""
from django.db import models


class Event(models.Model):
    """
    Event model class.
    """
    name = models.CharField(max_length=255)
    date = models.DateField()
    hosted_in = models.CharField(max_length=255)
    host_website = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)



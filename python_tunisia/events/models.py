"""
Events model module.
"""
"""
Event model module.
"""
from django.db import models
from django.core.urlresolvers import reverse

from events.managers import EventManager


class Event(models.Model):
    """
    Event model class.
    """
    class Meta:
        ordering = ("-date", )

    name = models.CharField(max_length=255)
    date = models.DateField()
    hosted_in = models.CharField(max_length=255)
    host_name = models.CharField(max_length=255)
    host_website = models.URLField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = EventManager()

    def get_absolute_url(self):
        return reverse("event_details_view", args=[str(self.id)])


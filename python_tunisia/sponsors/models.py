"""
Sponsor model module.
"""
from django.db import models
from django.core.urlresolvers import reverse

from sponsors.managers import SponsorsManager


class Sponsor(models.Model):
    """
    Sponsor model class.
    """
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = SponsorsManager()

    def get_absolute_url(self):
        return reverse("sponsor_details_view", args=[str(self.id)])


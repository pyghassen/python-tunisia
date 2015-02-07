"""
Company model module.
"""
from django.db import models
from django.core.urlresolvers import reverse

from companies.managers import CompaniesManager


class Company(models.Model):
    """
    Company model class.
    """
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = CompaniesManager()

    def get_absolute_url(self):
        return reverse("developer_details_view", args=[str(self.id)])


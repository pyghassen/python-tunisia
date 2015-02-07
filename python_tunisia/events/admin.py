"""
Event Admin module.
"""
from django.contrib import admin

from events.models import Event


class EventAdmin(admin.ModelAdmin):
    """
    Custom Admin for event on Django Administration.
    """
    list_display = (
        "name", 'date', 'hosted_in', "created_at",
    )

admin.site.register(Event, EventAdmin)


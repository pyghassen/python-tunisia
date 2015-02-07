"""
Event Manager module.
"""
from datetime import datetime

from django.db.models import Manager


class EventManager(Manager):
    """
    Event Manager class.
    """
    def past_events(self):
        """
        Returns the past event.
        """
        return self.filter(date__lt=datetime.today(), is_active=True)

    def future_events(self):
        """
        Returns the future events.
        """
        return self.filter(date__gte=datetime.today(), is_active=True)



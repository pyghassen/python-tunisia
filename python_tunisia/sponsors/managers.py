"""
Sponsors Manager module.
"""
from django.db.models import Manager


class SponsorsManager(Manager):
    """
    Sponsors Manager class.
    """
    def get_query_set(self):
        """
        Returns the active sponsors only.
        """
        return super().get_query_set().filter(is_active=True)

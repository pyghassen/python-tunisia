"""
Sponsors Manager module.
"""
from django.db.models import Manager


class SponsorsManager(Manager):
    """
    Sponsors Manager class.
    """
    def get_queryset(self):
        """
        Returns the active sponsors only.
        """
        return super().get_queryset().filter(is_active=True)

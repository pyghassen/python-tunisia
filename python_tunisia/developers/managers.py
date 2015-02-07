"""
Developers Manager module.
"""
from django.db.models import Manager


class DevelopersManager(Manager):
    """
    Developers Manager class.
    """
    def get_queryset(self):
        """
        Returns the active developers only.
        """
        return super().get_queryset().filter(is_active=True)



"""
Companies Manager module.
"""
from django.db.models import Manager


class CompaniesManager(Manager):
    """
    Companies Manager class.
    """
    def get_queryset(self):
        """
        Returns the active companies only.
        """
        return super().get_queryset().filter(is_active=True)

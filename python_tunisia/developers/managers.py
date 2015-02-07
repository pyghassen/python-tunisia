"""
Developers Manager module.
"""
from django.db.models import Manager


class DevelopersManager(Manager):
    """
    Developers Manager class.
    """
    def get_query_set(self):
        """
        Returns the active developers only.
        """
        return super().get_query_set().filter(is_active=True)



"""
Companies Manager module.
"""
from django.db.models import Manager


class CompaniesManager(Manager):
    """
    Companies Manager class.
    """
    def get_query_set(self):
        """
        Returns the active companies only.
        """
        return super().get_query_set().filter(is_active=True)

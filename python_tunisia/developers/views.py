"""
Developers views module.
"""
from django.views.generic import ListView, DetailView
from developers.models import Developer


class ListDevelopersView(ListView):
    """
    List Developers View class.
    """
    model = Developer

class DeveloperDetailsView(DetailView):
    """
    Developer Details View class.
    """
    model = Developer

list_developers_view = ListDevelopersView.as_view()
developer_details_view = DeveloperDetailsView.as_view()

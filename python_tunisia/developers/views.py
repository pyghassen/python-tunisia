"""
Developers views module.
"""
from developers.models import Developer
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView


class CreateDeveloperView(CreateView):
	"""
	Create Developer View class.
	"""
	model = Developer

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

"""
Sponsors views module.
"""
from django.views.generic import ListView, DetailView
from sponsors.models import Sponsor


class ListSponsorsView(ListView):
    """
    List Sponsors View class.
    """
    model = Sponsor

class SponsorDetailsView(DetailView):
    """
    Sponsor Details View class.
    """
    model = Sponsor

list_sponsors_view = ListSponsorsView.as_view()
sponsor_details_view = SponsorDetailsView.as_view()

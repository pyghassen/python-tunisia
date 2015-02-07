"""
Companies views module.
"""
from django.views.generic import ListView, DetailView
from companies.models import Company


class ListCompaniesView(ListView):
    """
    List Companies View class.
    """
    model = Company

class CompanyDetailsView(DetailView):
    """
    Company Details View class.
    """
    model = Company

list_companies_view = ListCompaniesView.as_view()
company_details_view = CompanyDetailsView.as_view()
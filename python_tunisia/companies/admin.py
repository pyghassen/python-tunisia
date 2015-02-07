"""
Company Admin module.
"""
from django.contrib import admin

from companies.models import Company


class CompanyAdmin(admin.ModelAdmin):
    """
    Custom Admin for companies on Django Administration.
    """
    list_display = (
        "name", "created_at",
    )

admin.site.register(Company, CompanyAdmin)

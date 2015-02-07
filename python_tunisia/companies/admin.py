"""
Company Admin module.
"""
from django.contrib import admin

from sponsors.models import Company


class CompanyAdmin(admin.ModelAdmin):
    """
    Custom Admin for Companies on Django Administration.
    """
    list_display = (
        "name", "created_at",
    )

admin.site.register(Company, CompanyAdmin)

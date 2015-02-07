"""
Sponsor Admin module.
"""
from django.contrib import admin

from sponsors.models import Sponsor


class SponsorAdmin(admin.ModelAdmin):
    """
    Custom Admin for sponsors on Django Administration.
    """
    list_display = (
        "name", "created_at",
    )

admin.site.register(Sponsor, SponsorAdmin)


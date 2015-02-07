"""
Developer Admin module.
"""
from django.contrib import admin

from developers.models import Developer


class DeveloperAdmin(admin.ModelAdmin):
    """
    Custom Admin for developers on Django Administration.
    """
    list_display = (
        "name", "created_at",
    )

admin.site.register(Developer, DeveloperAdmin)

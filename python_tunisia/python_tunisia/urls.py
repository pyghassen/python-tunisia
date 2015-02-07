from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
# from django.views.decorators.cache import cache_page

from jobs.views import JobView


urlpatterns = patterns('',
    url(
        r'^$',
        TemplateView.as_view(template_name="home.html"),
        name='home'
    ),
    url(
        r'^about/$',
        TemplateView.as_view(template_name="about.html"),
        name='about'
    ),
    url(
        r'^download/$',
        TemplateView.as_view(template_name="download.html"),
        name='download'
    ),
    url(
        r'^jobs/$',
        JobView.as_view(template_name="jobs.html"),
        name='jobs'
    ),
    url(
        r'^events/$',
        "events.views.list_events_view",
        name='events'
    ),
    url(
        r'^events/(?P<pk>\d+)$',
        "events.views.event_details_view",
        name='event_details_view'
    ),
    url(
        r'^companies/$',
        "companies.views.list_companies_view",
        name='companies'
    ),
    url(
        r'^companies/(?P<pk>\d+)$',
        "companies.views.company_details_view",
        name='company_details_view'
    ),
    url(
        r'^developers/$',
        "developers.views.list_developers_view",
        name='developers'
    ),
    url(
        r'^developers/(?P<pk>\d+)$',
        "developers.views.developer_details_view",
        name='developer_details_view'
    ),
    url(
        r'^sponsors/$',
        "sponsors.views.list_sponsors_view",
        name='sponsors'
    ),
    url(
        r'^sponsors/(?P<pk>\d+)$',
        "sponsors.views.sponsor_details_view",
        name='sponsor_details_view'
    ),

    url(r'^admin/', include(admin.site.urls)),
    # (r'^accounts/', include('allauth.urls')),
    # url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
    url(r'^contact/', include('django_contactme.urls')),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),

    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
)

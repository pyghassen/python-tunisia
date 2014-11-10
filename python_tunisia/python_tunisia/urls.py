from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from jobs.views import JobView


urlpatterns = patterns('',
    url(
        r'^$',
        cache_page(60 * 60 * 24)(TemplateView.as_view(template_name="home.html")),
        name='home'
    ),
    url(
        r'^about/$',
        #cache_page(60 * 60 * 24)(
            TemplateView.as_view(template_name="about.html")
            #)
        ,
        name='about'
    ),
    url(
        r'^download/$',
        #cache_page(60 * 60 * 24)(
            TemplateView.as_view(template_name="download.html")
            #)
        ,
        name='download'
    ),
    url(
        r'^jobs/$',
        #cache_page(60 * 60 * 24)(
            JobView.as_view(template_name="jobs.html")
            #)
        ,
        name='jobs'
    ),

    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
    url(r'^contact/', include('django_contactme.urls')),
)

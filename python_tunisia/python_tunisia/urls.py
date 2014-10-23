from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page


urlpatterns = patterns('',
    url(
        r'^$',
        #cache_page(60 * 60 * 24)(
            TemplateView.as_view(template_name="home.html")
            #)
        ,
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

    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
)

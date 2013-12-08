"""
Backwards-compatible URLconf for existing django-registration
installs; this allows the standard ``include('registration.urls')`` to
continue working, but that usage is deprecated and will be removed for
django-registration 1.0. For new installs, use
``include('registration.backends.default.urls')``.

"""


from registration.backends.default.urls import *
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, ListView, DetailView
from travelsite.destinations.models import *
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'travelsite.destinations.views.index'),
    url(r'^destinations/', include('travelsite.destinations.urls')),
    url(r'^accounts/', include('travelsite.registration.backends.default.urls')),
    url(r'^contact/$',
        TemplateView.as_view(
            template_name='destinations/contact.html'
    )),
    url(r'^about/$',
        TemplateView.as_view(
            template_name='destinations/about.html'
    )),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include('travelsite.profiles.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.`.serve', {
        'document_root': settings.MEDIA_ROOT})
)

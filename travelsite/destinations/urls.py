from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, ListView, DetailView
from travelsite.destinations.models import *

urlpatterns = patterns('',
    url(r'^$', 'travelsite.destinations.views.index'),
    url(r'^byinterest/$',
        ListView.as_view(
            queryset=Interest.objects.all(),
            context_object_name='interest_list',
    )),
    url(r'^bycity/$',
        ListView.as_view(
            queryset=City.objects.all(),
            context_object_name='city_list',
    )),
    url(r'^bycountry/$',
        ListView.as_view(
            queryset=Country.objects.all(),
            context_object_name='country_list',
    )),
    url(r'^map/$',
        TemplateView.as_view(
            template_name='destinations/map.html',
    )),
    url(r'^countries/(?P<country_id>\d+)/$', 'travelsite.destinations.views.country_detail'),
    url(r'^cities/(?P<city_id>\d+)/$', 'travelsite.destinations.views.city_detail'),
    url(r'^(?P<destination_id>\d+)/$', 'travelsite.destinations.views.dest_detail'),
    url(r'^(?P<review_id>\d+)/$',
        TemplateView.as_view(
            template_name='destinations/review.html'
    )),
    url(r'dest_form/$', 'travelsite.destinations.views.dest_form_view'),
    url(r'review_form/$', 'travelsite.destinations.views.review_form_view'),
    url(r'country_form/$', 'travelsite.destinations.views.country_form_view'),
    url(r'city_form/$', 'travelsite.destinations.views.city_form_view'),
    url(r'form_home/$',
        TemplateView.as_view(
            template_name='destinations/form_home.html',
    )),
 
    url(r'dest_form_complete/$',
        TemplateView.as_view(
            template_name='destinations/dest_form_complete.html',
    )),
    url(r'profile_form/$',
        TemplateView.as_view(
            template_name='destinations/profile_form.html',
)),
)


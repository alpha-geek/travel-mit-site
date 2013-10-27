
from django.conf.urls.defaults import patterns, include, url
from travelsite.forum.models import *

urlpatterns = patterns('',

    url(r'^main/$', 'travelsite.forum.views.main'),
    url(r'^forum/(\d+)/$','travelsite.forum.views.forum'),
    url(r'thread/(\d+)/$','travelsite.forum.views.thread'),
)

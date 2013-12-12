"""

This file registers the destination classes into the admin site.

"""

from travelsite.destinations.models import *
from django.contrib import admin

admin.site.register(Destination)
admin.site.register(Interest)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Review)

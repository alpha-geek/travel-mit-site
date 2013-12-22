"""

Destination views.

"""
# pylint: disable=C1001,W0403,W0232,E1101,R0903

from django.template import Context, loader, RequestContext
from travelsite.destinations.models import Destination, DestForm, City, Country, CityForm, CountryForm, Review, ReviewForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.forms.models import modelformset_factory
from django.core.context_processors import csrf

def dest_form_view(request):
    """View for destination creation form."""
    c = {}
    c.update(csrf(request))
    a = Destination()
    if request.method == 'POST':
        dest_form = DestForm(request.POST, instance=a)
        if dest_form.is_valid():
            a = dest_form.save()
            return HttpResponseRedirect('destinations/dest_form_complete/')
    else:
        dest_form = DestForm(instance=a)
    return render_to_response('destinations/dest_form.html', {
        'dest_form': dest_form,
    }, context_instance=RequestContext(request))

def review_form_view(request):
    """View for review creation form."""
    c = {}
    c.update(csrf(request))
    a = Review()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=a)
        if review_form.is_valid():
            a = review_form.save()
            return HttpResponseRedirect('destinations/dest_form_complete/')
    else:
        review_form = ReviewForm(instance=a)
    return render_to_response('destinations/review_form.html', {
        'review_form': review_form,
    }, context_instance=RequestContext(request))

def city_form_view(request):
    """View for city creation form."""
    c = {}
    c.update(csrf(request))
#    if request.method == 'POST':
    a = City()
    if request.method == 'POST':
        city_form = CityForm(request.POST, instance=a)
        if city_form.is_valid():
            city_form.save()
            return HttpResponseRedirect('destinations/dest_form_complete/')
    else:
        city_form = CityForm(instance=a)
    return render_to_response('destinations/city_form.html', {
        'city_form': city_form,
    }, context_instance=RequestContext(request))

def country_form_view(request):
    """View for country creation form."""
    c = {}
    c.update(csrf(request))
#    if request.method == 'POST':
    a = Country()
    if request.method == 'POST':
        country_form = CountryForm(request.POST, instance=a)
        if country_form.is_valid():
            country_form.save()
            return HttpResponseRedirect('destinations/dest_form_complete/')
    else:
        country_form = CountryForm(instance=a)
    return render_to_response('destinations/country_form.html', {
        'country_form': country_form,
    }, context_instance=RequestContext(request))


def dest_edit_form_view(request):
    """View to edit a destination."""
    c = {}
    c.update(csrf(request))
    FormSet = modelformset_factory(Destination, exclude=('address',))
    if request.method == 'POST':
        formset = FormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = FormSet(queryset=Destination.objects.all()
)
    return render_to_response('destinations/dest_edit_form.html', {
        'formset': formset,
    }, context_instance=RequestContext(request))

def review_form_edit_view(request):
    """View to edit a review."""
    c = {}
    c.update(csrf(request))
    FormSet = modelformset_factory(Review)
    if request.method == 'POST':
        formset = FormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = FormSet
    return render_to_response('destinations/review_edit_form.html', {
        'formset': formset,
    }, context_instance=RequestContext(request))

def country_form_edit_view(request):
    """View to edit a country."""
    c = {}
    c.update(csrf(request))
    FormSet = modelformset_factory(Country)
    if request.method == 'POST':
        formset = FormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = FormSet
    return render_to_response('destinations/country_edit_form.html', {
        'formset': formset,
    }, context_instance=RequestContext(request))

def city_form_edit_view(request):
    """View to edit a city."""
    c = {}
    c.update(csrf(request))
    FormSet = modelformset_factory(CityForm)
    if request.method == 'POST':
        formset = FormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = FormSet()
    return render_to_response('destinations/city_edit_form.html', {
        'formset': formset,
    }, context_instance=RequestContext(request))

def index(request):
    """Index of destinations."""
    latest_destination_list = Destination.objects.all().order_by('-id')[:3]
    t = loader.get_template('destinations/index.html')
    c = RequestContext(request, {
        'latest_destination_list': latest_destination_list,
    })
    return HttpResponse(t.render(c))

def dest_detail(request, destination_id):
    """Specific destination view."""
    p = get_object_or_404(Destination, pk=destination_id)
    name = p.name
    review_list = p.review_set.all().order_by('-id')[:5]
    city = p.city
    t = loader.get_template('destinations/dest_detail.html')
    c = Context({
        'name': name,
        'review_list': review_list,
        'city': city,
    })
    return HttpResponse(t.render(c))

def country_detail(request, country_id):
    """Specific country view."""
    d = get_object_or_404(Country, pk=country_id)
    related_cities_list = d.cities
    t = loader.get_template('destinations/country_detail.html')
    name = d.country_name
    c = Context ({
        'name': name,
        'related_cities_list': related_cities_list,
    })
    return HttpResponse(t.render(c))

def city_detail(request, city_id):
    """Specific city view."""
    d = get_object_or_404(City, pk=city_id)
    name = d.city_name
    destination_list = d.destination_set.all().order_by('-id')[:5]
    parent_country = d.parent_country
    t = loader.get_template('destinations/city_detail.html')
    c = Context ({
        'name': name,
        'destination_list': destination_list,
        'parent_country': parent_country,
    })
    return HttpResponse(t.render(c))

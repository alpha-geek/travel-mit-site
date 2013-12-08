from django.template import Context, loader, RequestContext
from travelsite.destinations.models import Destination, Dest_Form, City, Country, Interest, City_Form, Country_Form, Review, Review_Form
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.core.context_processors import csrf
#from django.views.decorators.csrf import csrf_protect
def handle_uploaded_file(f):
    fileplace = open('some/file/name.txt','wb+')
    for chunk in f.chunks():
        fileplace.write(chunk)
    fileplace.close()

#def upload_file(request):
#    if request.method == 'POST':
#        form = UploadFileForm(request.POST, request.FILES)
#        if form.is_valid():
#        handle_uploaded_file(request.FILES['file'])
#        return HttpResponseRedirect('/success/url/')
#    else:
#        form = UploadFileForm()
#    return render_to_response('upload.html', {'form': form})

def dest_form_view(request):
    c = {}
    c.update(csrf(request))
#    if request.method == 'POST':
    a = Destination()
    if request.method == 'POST':
        dest_form = Dest_Form(request.POST, instance=a)
        if dest_form.is_valid():
            a = dest_form.save()
            return HttpResponseRedirect('destinations/dest_form_complete/')
            pass
    else:
        dest_form = Dest_Form(instance=a)
    return render_to_response('destinations/dest_form.html', {
        'dest_form': dest_form,
    }, context_instance=RequestContext(request))

def review_form_view(request):
    c = {}
    c.update(csrf(request))
#    if request.method == 'POST':
    a = Review()
    if request.method == 'POST':
        review_form = Review_Form(request.POST, instance=a)
        if review_form.is_valid():
            a = review_form.save()
            return HttpResponseRedirect('destinations/dest_form_complete/')
            pass
    else:
        review_form = Review_Form(instance=a)
    return render_to_response('destinations/review_form.html', {
        'review_form': review_form,
    }, context_instance=RequestContext(request))

def city_form_view(request):
    c = {}
    c.update(csrf(request))
#    if request.method == 'POST':
    a = City()
    if request.method == 'POST':
        city_form = City_Form(request.POST, instance=a)
        if city_form.is_valid():
            city_form.save()
            return HttpResponseRedirect('destinations/dest_form_complete/')
            pass
    else:
        city_form = City_Form(instance=a)
    return render_to_response('destinations/city_form.html', {
        'city_form': city_form,
    }, context_instance=RequestContext(request))

def country_form_view(request):
    c = {}
    c.update(csrf(request))
#    if request.method == 'POST':
    a = Country()
    if request.method == 'POST':
        country_form = Country_Form(request.POST, instance=a)
        if country_form.is_valid():
            country_form.save()
            return HttpResponseRedirect('destinations/dest_form_complete/')
            pass
    else:
        country_form = Country_Form(instance=a)
    return render_to_response('destinations/country_form.html', {
        'country_form': country_form,
    }, context_instance=RequestContext(request))


def dest_edit_form_view(request):

    c = {}
    c.update(csrf(request))
 #   form = models.Dest_Form(request.POST)
    FormSet = modelformset_factory(Destination, exclude=('address',))
    if request.method == 'POST':
        formset = FormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
#            formset.save_m2m()
            pass
    else:
        formset = FormSet(queryset=Destination.objects.all()
)
    return render_to_response('destinations/dest_edit_form.html', {
        'formset': formset,
    }, context_instance=RequestContext(request)) 

def review_form_edit_view(request):

   c = {} 
   c.update(csrf(request))
#    form = models.Review_Form(request.POST)
   FormSet = modelformset_factory(Review)

   if request.method == 'POST':

       formset = FormSet(request.POST, request.FILES)

       if formset.is_valid():
           formset.save()
#           formset.save_m2m()
           pass
   else:
       formset = FormSet
   return render_to_response('destinations/review_edit_form.html', {
       'formset': formset,
   }, context_instance=RequestContext(request))

def country_form_edit_view(request):

    c = {}
    c.update(csrf(request))
 #   form = models.Country_Form(request.POST)
    FormSet = modelformset_factory(Country)
    if request.method == 'POST':
        formset = FormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
#            formset.save_m2m()
            pass
    else:
           formset = FormSet
    return render_to_response('destinations/country_edit_form.html', {
        'formset': formset,
    }, context_instance=RequestContext(request))

def city_form_edit_view(request):

    c = {}
    c.update(csrf(request))
#    form = models.City_Form(request.POST)
    FormSet = modelformset_factory(City_Form)
    if request.method == 'POST':
        formset = FormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
#            formset.save_m2m()
            pass
    else:
           formset = FormSet()
    return render_to_response('destinations/city_edit_form.html', {
        'formset': formset,
    }, context_instance=RequestContext(request))

def index(request):
    latest_destination_list = Destination.objects.all().order_by('-id')[:5]
    t = loader.get_template('destinations/index.html')
    c = RequestContext(request, {
        'latest_destination_list': latest_destination_list,
    })
    return HttpResponse(t.render(c))

def dest_detail(request, destination_id):
    p = get_object_or_404(Destination, pk=destination_id)
    name = p.name
    review_list = p.review_set.all().order_by('-id')[:5]
    city = p.city,
#    q = get_object_or_404(City, pk=city.id)
 #   country = q.parent_country,
    t = loader.get_template('destinations/dest_detail.html')
#    related_interests = p.interest.order_by('-id')
    c = Context({
        'name': name,
        'review_list': review_list,
        'city': city,
#        'country': country,
#        'related_interests': related_interests
    })
    return HttpResponse(t.render(c))

def country_detail(request, country_id):
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
    d = get_object_or_404(City, pk=city_id)
    name = d.city_name
    destination_list = d.destination_set.all().order_by('-id')[:5]
    parent_country = d.parent_country
  #  related_interests = d.interest.order_by('-id')
    t = loader.get_template('destinations/city_detail.html')
    c = Context ({
        'name': name,
        'destination_list': destination_list,
   #     'related_interests': related_interests,
        'parent_country': parent_country,
    })
    return HttpResponse(t.render(c))

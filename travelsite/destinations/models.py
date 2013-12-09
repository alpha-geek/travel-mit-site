from django.db import models
from django import forms
from django.forms import ModelForm


class Interest(models.Model):
    interest_name = models.CharField(max_length=20) 

    class Meta:
        ordering = ('interest_name',)

    def __unicode__(self):
        return self.interest_name

class Rating(models.Model):
    rating_value = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['-rating_value']

class Country(models.Model):
    country_name = models.CharField(max_length=20)    

    class Meta:
        ordering = ('country_name',)

    def __unicode__(self):
        return self.country_name

    def cities(self):
        return self.city_set.all().order_by('-id')

class City(models.Model):
    city_name = models.CharField(max_length=20)
    country = models.ForeignKey(Country)
#    basic_info = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.city_name

    class Meta:
        ordering = ('city_name',)

    def parent_country(self):
        return self.country

class Destination(models.Model):
    name = models.CharField(max_length=50)

#   consider adding gpscoord to integrate with google maps?
    city = models.ForeignKey(City)
    interest = models.ManyToManyField(Interest, null=True, blank=True)
#    basic_info = models.TextField(null=True, blank=True)
#    pub_date = models.DateTimeField('date published')
    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class Review(models.Model):
    review_headline = models.CharField(max_length=50)
    review_content = models.TextField()
    destination = models.ForeignKey(Destination)
    rating = models.IntegerField(null=True, blank=True)

class Dest_Form(ModelForm):
    class Meta:
        model = Destination
#    def save(self):
 #       if self.is_valid():
  #          from travelsite.destinations.models import Destination
   #         new_destination = Destination(**self.cleaned_data)
    #        new_destination.save()
     #       return new_friend

class City_Form(ModelForm):

    class Meta:
        model = City
        fields = ('city_name','country')

#    def save(self, commit=True):
#        city = super(City, self).save(commit=False)
#        city.inuse = True
#        if commit:
#            city.save()

class Country_Form(ModelForm):
    class Meta:
        model = Country
    country_name = models.CharField(max_length=20)


class Review_Form(ModelForm):
    class Meta:
        model = Review

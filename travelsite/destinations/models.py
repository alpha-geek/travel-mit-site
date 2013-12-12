"""

This file contains the models relating to the destination class,
including city, country, destination, interest, and forms.

"""

from django.db import models
from django.forms import ModelForm

class Interest(models.Model):
    """Interest model, which will have a ManyToMany relation
    with Destinations"""
    interest_name = models.CharField(max_length=20)
    class Meta:
        """Meta class for lists and forms"""
        ordering = ('interest_name',)

    def __unicode__(self):
        return self.interest_name

class Rating(models.Model):
    """Rating model, there is already a ratings attribute for reviews
    so this may be removed"""
    rating_value = models.IntegerField(null=True, blank=True)
    class Meta:
        """Meta class for lists and forms"""
        abstract = True
        ordering = ['-rating_value']

class Country(models.Model):
    """Country model"""
    country_name = models.CharField(max_length=20)
    class Meta:
        """Meta class for lists and forms"""
        ordering = ('country_name',)

    def __unicode__(self):
        return self.country_name

    def cities(self):
        """Return list of cities in country"""
        return self.city_set.all().order_by('-id')

class City(models.Model):
    """City model, many to one relation to country and one to many relation
    to destination, may have to change to many to many with destination"""
    city_name = models.CharField(max_length=20)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.city_name
    class Meta:
        """Meta class for lists and forms"""
        ordering = ('city_name',)

    def parent_country(self):
        """Returns parent country"""
        return self.country

class Destination(models.Model):
    """Destination model, with a parent city, ManyToMany interest setup,
    and one to many review setup"""
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City)
    interest = models.ManyToManyField(Interest, null=True, blank=True)
    class Meta:
        """Meta class for lists and forms"""
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class Review(models.Model):
    """Review model, may rename headline in form and/or model"""
    review_headline = models.CharField(max_length=50)
    review_content = models.TextField()
    destination = models.ForeignKey(Destination)
    rating = models.IntegerField(null=True, blank=True)

class DestForm(ModelForm):
    """Destination form, inherits from ModelForm"""
    class Meta:
        """Meta class for forms"""
        model = Destination

class CityForm(ModelForm):
    """City form, inherits from ModelForm"""
    class Meta:
        """Meta class for forms"""
        model = City
        fields = ('city_name','country')

class CountryForm(ModelForm):
    """Country form, inherits from ModelForm"""
    class Meta:
        """Meta class for forms"""
        model = Country
    country_name = models.CharField(max_length=20)

class ReviewForm(ModelForm):
    """Review form, inherits from ModelForm"""
    class Meta:
        """Meta class for forms"""
        model = Review

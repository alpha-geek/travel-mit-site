from django.db import models
from django.forms import ModelForm
from travelsite.profiles.models import *
 
class ProfileForm(ModelForm):
  class Meta:
      model = Profile
      exclude = ('id','posts',)

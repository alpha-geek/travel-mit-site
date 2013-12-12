"""

Profile Form, which inherits from Django's ModelForm.

"""

from django.db import models
from django.forms import ModelForm
from travelsite.profiles.models import *
 
class ProfileForm(ModelForm):
	"""
	Profile Form which allows user to create and edit properties excluding id and posts.
	"""
	class Meta:
      model = Profile
      exclude = ('id','posts',)

from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm

class userinfo(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['user','dob','univ','gender','aboutme']

class abc(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','email']
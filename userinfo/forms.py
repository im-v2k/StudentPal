from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm

class userinfo(forms.ModelForm):
	univ = forms.CharField(max_length=50, disabled=True)
	class Meta:
		model = Profile
		fields = ['dob', 'univ', 'gender', 'aboutme']

class abc(forms.ModelForm):
	username = forms.CharField(max_length=150, disabled=True)
	class Meta:
		model = User
		fields = ['username', 'first_name','last_name','email']

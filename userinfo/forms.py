from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm

class profileinfo1(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['dob','univ','gender','aboutme']

class userinfo1(forms.ModelForm):
	username = forms.CharField(max_length=150,disabled=True)
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']

class profileinfo2(forms.ModelForm):
	dob = forms.DateField(disabled=True)
	univ = forms.CharField(disabled=True)
	gender = forms.CharField(widget=forms.Select(
		choices=(('N', 'I prefer not to say'),
			('M', 'Male'),
			('F', 'Female'),
			('O', 'Other'))),disabled=True)
	aboutme = forms.CharField(disabled=True,widget=forms.Textarea)
	class Meta:
		model = Profile
		fields = ['dob','univ','gender','aboutme']

class userinfo2(forms.ModelForm):
	username = forms.CharField(max_length=150,disabled=True)
	first_name = forms.CharField(max_length=30,disabled=True)
	last_name = forms.CharField(max_length=30,disabled=True)
	email = forms.EmailField(disabled=True,label="Email address")
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']

## @file forms.py
#  @author SYNTAX
#  @date 28 Oct 2017
#  
#  @brief This is a file conatining some classes using python.
#
#  It contains classes named event_details,update_detail, delete_details 
#  The arguments describe the type of functions described in the class.
from django import forms
from .models import *
from django.forms import ModelForm


## class event_details 
#
# maintains data related to events of user
# name,date,description are some of its parts
#
class event_details(forms.Form):
	name = forms.CharField(max_length=30)
	date = forms.DateField()
	start_time = forms.TimeField()
	end_time = forms.TimeField()
	description = forms.CharField(widget=forms.Textarea)

	def clean(self):
		cleaned_data = super(event_details,self).clean()
		name = cleaned_data.get('name')
		date = cleaned_data.get('date')
		start_time = cleaned_data.get('start_time')
		end_time = cleaned_data.get('end_time')
		description = cleaned_data.get('description')
		if not name and not date and not start_time and not end_time and not description:
			raise forms.ValidationError('This has to be filled')

## class update_detail
#
# Used to update details related to events of user
# related to fields named name,date,description etc.
#
class update_detail(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['name','date','start_time','end_time','description']

## class delete_details
#
# Used to delete details related to events of user
#
class delete_details(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['name']

	def clean(self):
		cleaned_data = super(delete_details,self).clean()
		name = cleaned_data.get('name')
		if not name:
			raise forms.ValidationError('This has to be filled')

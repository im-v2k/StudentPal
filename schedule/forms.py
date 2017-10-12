from django import forms

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

class update_details(forms.Form):
	name = forms.CharField(max_length=30)
	date = forms.DateField()
	start_time = forms.DateTimeField()
	end_time = forms.DateTimeField()
	description = forms.CharField(widget=forms.Textarea)
	get_notifications = forms.BooleanField(widget=forms.CheckboxInput)

	def clean(self):
		cleaned_data = super(update_details,self).clean()
		name = cleaned_data.get('name')
		date = cleaned_data.get('date')
		start_time = cleaned_data.get('start_time')
		end_time = cleaned_data.get('end_time')
		description = cleaned_data.get('description')
		if not name and not date and not start_time and not end_time and not description:
			raise forms.ValidationError('This has to be filled')

class delete_details(forms.Form):
	name = forms.CharField(max_length=30)

	def clean(self):
		cleaned_data = super(delete_details,self).clean()
		name = cleaned_data.get('name')
		if not name:
			raise forms.ValidationError('This has to be filled')

from django import forms
from .models import FakeCourse

class new_group(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super(new_group,self).clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        if not name:
            raise forms.ValidationError('This has to be filled')

class search_group(forms.Form):
    string = forms.CharField(max_length=50, label="Find a group ")

class new_course(forms.ModelForm):
    name = forms.CharField(max_length=20, label="Add a course")
    class Meta:
        model = FakeCourse
        fields = ['name']

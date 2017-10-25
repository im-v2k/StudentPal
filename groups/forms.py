from django import forms

class new_group(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super(new_group,self).clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        if not name:
            raise forms.ValidationError('This has to be filled')

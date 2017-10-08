from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    
    first_name = forms.CharField(
        label=_("First name"),
        max_length=20,
        required=True
    )
    last_name = forms.CharField(
        label=_("Last name"),
        max_length=20,
        required=False
    )
    email = forms.EmailField(
        label=_("Email Address"),
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "first_name", "last_name", "email")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

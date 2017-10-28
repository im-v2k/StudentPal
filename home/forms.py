## @file forms.py
#  @author SYNTAX
#  @date 28 Oct 2017
#  
#  @brief This is a file conatining some classes using python.
#
#  It contains class named CustomUserCreationForm
#  The arguments describe the type of functions described in the class.
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField

## class CustomUserCreationForm
#
# It is a form used to create new user
#first_name,last_name,email etc. are its parts
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
        required=True,
        help_text=_("Your email address is used to send you notifications, performance reports and also in case of a password reset.")
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=_("Enter a password that is easy to remember and hard to guess.")
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "first_name", "last_name", "email")
        field_classes = {'username': UsernameField}
    ## Used to save new user data to database
    # 
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

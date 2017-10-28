## @file views.py
#  @author SYNTAX
#  @date 28 Oct 2017
#  
#  @brief This is a file conatining some functions using python.
#
#  It contains of two functions named homepage,signup etc.
#  The arguments describe the type of functions described in the class.

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from home.forms import CustomUserCreationForm

## Function homepage
#  @return Redirects to home.html page
def homepage(request):
    return render(request, 'home/home.html')


## Function signup
#
#  @details It takes details of new user.
#  @return Redirects to signup.html page
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = CustomUserCreationForm()
    return render(request, 'home/signup.html', {'form': form})

## Function mylogout
#
#  @details It is requested when wanted to logout.
#  @return Redirects to logout.html page
def mylogout(request):
    if request.method == 'POST':
        return logout(request, template_name='home/logged_out.html')
    else:
        return render(request, 'home/logout.html')

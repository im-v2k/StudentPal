from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from home.forms import CustomUserCreationForm

def homepage(request):
	return render(request, 'home/home.html')

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

def mylogout(request):
	if request.method == 'POST':
		return logout(request, template_name='home/logged_out.html')
	else:
		return render(request, 'home/logout.html')


# def test(request):
# 	return render(request, 'home/test.html')

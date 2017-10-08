from django.shortcuts import render
#from home.forms import CustomUserCreationForm

def info(request):
	return render(request, 'userinfo/info.html')
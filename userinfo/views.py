from django.shortcuts import render,redirect,reverse
import sys
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from datetime import datetime

def info(request):
	if 'edit' in request.POST:
		disable = false
		info = userinfo()
		user = User()
		return render(request, 'userinfo/info.html',{'info' : info,'disable' : disable,'user': user})
	elif 'save' in request.POST:
		disable = true
		info = userinfo()
		user = abc()
		return render(request, 'userinfo/info.html',{'info' : info,'disable' : disable,'user' : user})
	else:
		info = userinfo()
		user = abc()
		return render(request, 'userinfo/info.html',{'info' : info,'user' : user})
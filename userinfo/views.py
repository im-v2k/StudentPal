from django.shortcuts import render,redirect,reverse
import sys
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from datetime import datetime

def info(request):
	if request.user.is_authenticated():
		if 'edit' in request.POST:
			disable = False
			info = userinfo()
			userform = abc()
			return render(request, 'userinfo/info.html',{'info' : info,'disable' : disable,'userform': userform})
		elif 'save' in request.POST:
			disable = True
			info = userinfo()
			userform = abc()
			return render(request, 'userinfo/info.html',{'info' : info,'disable' : disable,'userform' : userform})
		else:
			user = request.user
			profile = user.profile
			info = userinfo(instance=profile)
			userform = abc(instance=user)
			return render(request, 'userinfo/info.html',{'info' : info,'userform' : userform})
	else:
		return render(request, 'userinfo/info.html')

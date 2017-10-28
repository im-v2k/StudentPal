## @file views.py
#  @author SYNTAX
#  @date 28 Oct 2017
#  
#  @brief This is a file conatining some functions using python.
#
#  It contains of functions named info,profileview etc.
from django.shortcuts import render,redirect,reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from datetime import datetime
from django.contrib import messages

## Function info
#
#  @details It deals with option to edit and save user information.
#  @return Redirects to info.html page
def info(request):
	if request.user.is_authenticated:
		if 'edit' in request.POST:
			a = True
			user = request.user
			profile = user.profile
			info1 = profileinfo1(instance=profile)
			info2 = userinfo1(instance=user)
			return render(request, 'userinfo/info.html',{'a' : a,'info1' : info1,'info2' : info2})
		elif 'save' in request.POST:
			a = False
			form = profileinfo1(request.POST)
			if form.is_valid():
				query = User.objects.get(username = request.user)
				form1  = profileinfo1(request.POST, instance = query.profile)
				form2  = userinfo1(request.POST, instance = query)
				form1.save()
				form2.save()
				if form2.is_valid():
					form2.save()
				else :
					messages.error(request,('Enter a valid email'))
			user = request.user
			profile = user.profile
			info1 = profileinfo2(instance=profile)
			info2 = userinfo2(instance=user)
			return render(request, 'userinfo/info.html',{'info1' : info1,'info2' : info2,'a' : a})
		else:
			a = False
			user = request.user
			profile = user.profile
			info1 = profileinfo2(instance=profile)
			info2 = userinfo2(instance=user)
			return render(request, 'userinfo/info.html',{'info1' : info1,'info2': info2,'a' : a})
		return HttpResponseRedirect('')
	else:
		return render(request, 'home/home.html')


## Function profileview
#  @return Redirects to profile.html page
def profileview(request, username):
	user = get_object_or_404(User, username=username)
	profile = user.profile
	info1 = profileinfo2(instance=profile)
	info2 = userinfo2(instance=user)
	return render(request, 'userinfo/profile.html',{'info1' : info1,'info2': info2})

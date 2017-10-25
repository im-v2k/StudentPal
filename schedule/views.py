from django.shortcuts import render,redirect,reverse
import sys
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from datetime import datetime
from django.contrib import messages

def events(request):
	events = Event.objects.all()
	return render(request,'schedule/events.html',{'events' : events})

def update_event(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		form = update_detail(request.POST)
		if form.is_valid():
			user = request.user
			if Event.objects.filter(name = name).exists():
				query = Event.objects.get(name = name)
				form1  = update_detail(request.POST, instance = query)
				form1.save()
			else :
				messages.error(request,('Enter a valid event name'))
		return HttpResponseRedirect('')
	else:
		form = update_detail()
		events = Event.objects.all()
	return render(request, 'schedule/update_event.html', {'events' : events,'form' : form})

def delete_event(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		form = delete_details(request.POST)
		if form.is_valid():
			user = request.user
			if Event.objects.filter(name = name).exists():
				query = Event.objects.get(name = name)
				query.delete()
			else :
				messages.error(request,('Enter a valid event name'))
			return HttpResponseRedirect('')
	else:
		form = delete_details()
		events = Event.objects.all()
	return render(request,'schedule/delete_event.html',{'events' : events,'form' : form})

def create_event(request):
	if request.method == 'POST':
		form = event_details(request.POST)
		if form.is_valid():
			user = request.user
			name = request.POST.get('name')
			if not Event.objects.filter(name = name).exists():
				date = request.POST.get('date')
				start_time = request.POST.get('start_time')
				end_time = request.POST.get('end_time')
				description = request.POST.get('description')
				event_obj = Event(user=user, name = name, date = date, start_time = start_time, end_time = end_time, description = description,)
				event_obj.save()
			else:
				messages.error(request,('An event with that name already exists'))
				return HttpResponseRedirect('')
			return render(request,'schedule/events.html')
	else:
		form = event_details()
	return render(request, 'schedule/new_event.html',{'form': form,})
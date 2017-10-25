from django.shortcuts import render,redirect,reverse
import sys
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from datetime import datetime

def events(request):
	return render(request,'schedule/events.html')

def update_event(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		form = update_detail(request.POST)
		if form.is_valid():
			user = request.user
			query = Event.objects.get(name = name)
			form1  = update_detail(request.POST, instance = query)
			form1.save()
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
			query = Event.objects.get(name = name)
			query.delete()
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
			date = request.POST.get('date')
			start_time = request.POST.get('start_time')
			end_time = request.POST.get('end_time')
			description = request.POST.get('description')
			event_obj = Event(user=user, name = name, date = date, start_time = start_time, end_time = end_time, description = description,)
			event_obj.save()

			return HttpResponseRedirect('')
	else:
		form = event_details()

	return render(request, 'schedule/new_event.html',{'form': form,})

def all_events(request):
	events = Event.objects.all()
	return render(request,'schedule/All_events.html',{'events' : events})

from django.shortcuts import render,redirect,reverse
from .forms import *
from .models import *

def events(request):
	return render(request,'schedule/events.html')
def new_event(request):
	form = event_details()
	return render(request,'schedule/new_event.html',{'form' : form})
def update_event(request):
	form = update_details()
	return render(request,'schedule/update_event.html',{'form' : form})
def delete_event(request):
	form = delete_details()
	return render(request,'schedule/delete_event.html',{'form' : form})

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

			return render(request,'schedule/created.html')
	else:
		form = event_details()

	return render(request, 'schedule/new_event.html',{'form': form,})
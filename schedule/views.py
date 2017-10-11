from django.shortcuts import render
from .forms import *

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

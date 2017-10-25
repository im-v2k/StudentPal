from django.conf.urls import url
from schedule import views as sched_views

urlpatterns = [
	url(r'^events/$',sched_views.events,name = 'events'),
	url(r'^update_event/$',sched_views.update_event,name = 'update_event'),
	url(r'^delete_event/$',sched_views.delete_event,name = 'delete_event'),
	url(r'^create/$',sched_views.create_event,name = 'create'),
]
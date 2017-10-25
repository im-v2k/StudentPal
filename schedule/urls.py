from django.conf.urls import url
from schedule import views as sched_views

urlpatterns = [
	url(r'^events/$',sched_views.events,name = 'events'),
	url(r'^create_event/$',sched_views.create_event,name = 'create_event'),
	url(r'^update_event/$',sched_views.update_event,name = 'update_event'),
	url(r'^update_details/$',sched_views.update_details,name = 'update_details'),
	url(r'^delete_event/$',sched_views.delete_event,name = 'delete_event'),
	url(r'^all_events/$',sched_views.all_events,name = 'all_events'),
]

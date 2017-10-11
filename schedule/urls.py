from django.conf.urls import url
from schedule import views as sched_views

urlpatterns = [
	url(r'^events/$',sched_views.events,name = 'events'),
	url(r'^new_event/$',sched_views.new_event,name = 'new_event'),
	url(r'^update_event/$',sched_views.update_event,name = 'update_event'),
	url(r'^delete_event/$',sched_views.delete_event,name = 'delete_event'),
]
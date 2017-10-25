from django.conf.urls import url
from groups import views

urlpatterns = [
	url(r'^$', views.mygroups, name='my_groups'),
	url(r'^new$', views.newgroup, name='new_group'),
	url(r'^search$', views.searchgroups, name='search_groups'),
	url(r'^(?P<pk>\d+)/$', views.particulargroup, name='particular_group')
]

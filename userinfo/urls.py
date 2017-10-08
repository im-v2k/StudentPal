from django.conf.urls import url
from userinfo import views as user_views

urlpatterns = [
	url(r'^info/$', user_views.info, name='user_info'),
]
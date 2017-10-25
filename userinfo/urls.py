from django.conf.urls import url
from userinfo import views as user_views

urlpatterns = [
	url(r'^info/$', user_views.info, name='user_info'),
	url(r'^user/(?P<username>\w+)/$', user_views.profileview, name='profileview')
]
from django.conf.urls import url
from home import views as home_views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', home_views.homepage, name='homepage'),
    url(r'^login/$', auth_views.login, {'template_name': 'home/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'home/logged_out.html'}, name='logout'),
    url(r'^signup/$', home_views.signup, name='signup'),
    url(r'^test/$', home_views.test, name='test')
]

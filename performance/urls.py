from django.conf.urls import url
from django.contrib import admin
from performance import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
	url(r'^courses/(?P<pk>\d+)/$', views.course_exams, name='course_exams'),
	url(r'^courses/(?P<pk>\d+)/new/$', views.new_exam, name='new_exam'),
    url(r'^courses/new_course/$', views.new_course, name='new_course'),
    url(r'^pdf/', views.some_view, name='some_view'),
    #url(r'^courses/pdf_prac/$',views.pdf_prac, name='pdf_prac'),
]

## @file views.py
#  @author SYNTAX
#  @date 28 Oct 2017
#  
#  @brief This is a file conatining some functions using python.
#
#  It contains of two functions named home,new_exam etc.
#  The arguments describe the type of functions described in the class.


## @package django.contrib.auth.models
from django.contrib.auth.models import User
## @package django.shortcuts
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Exam
## @package reportlab
from reportlab.pdfgen import canvas
## @package django.http
from django.http import HttpResponse, HttpResponseNotFound
## @package io
from io import BytesIO
## @package django.db.models
from django.db.models import Sum
import os, subprocess
## @package django.core.files.storage
from django.core.files.storage import FileSystemStorage

## Function home
#
#  @details It stores courses in variable named 'courses'
#  @return Redirects to home.html page
def home(request):
    u = User.objects.get(username=request.user)
    courses = u.course_set.all()
    return render(request, 'performance/home.html', {'courses': courses})

## Function course_exams
#
#  @details It stores courses in variable named 'courses'
#  @return Redirects to exams.html page
def course_exams(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'performance/exams.html', {'course': course})

## Function new_exam
#
#  @return Redirects to new_home.html page
def new_exam(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        name = request.POST['exam']
        weightage = request.POST['weightage']
        marks_obt = request.POST['marks_obt']
        max_marks = request.POST['max_marks']
        comment = request.POST['comment']


        user = User.objects.first()  #get the currently logged in user

        exam = Exam.objects.create(
            name=name,
            course=course,
            weightage=weightage,
            marks_obt=marks_obt,
            max_marks=max_marks,
            comment=comment,
        )

        exam.save()
        #comment.save()
        return redirect('course_exams', pk=course.pk)
    else:
        return render(request, 'performance/new_exam.html', {'course': course})

## Function new_course
#
#  @return Redirects to new_course.html page
def new_course(request):
    if request.method == 'POST':
        name = request.POST['course_name']
        code = request.POST['course_code']
        teacher = request.POST['prof']
        user = User.objects.get(username=request.user)
        course = user.course_set.create(
            name=name,
            teacher=teacher,
            code=code,
        )
        course.save()
        return redirect('home')
    return render(request, 'performance/new_course.html')


def som_view(request):
    subprocess.call('cd static/',shell=True)
    subprocess.call('pdflatex texfile',shell=True)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
    return response

def some_view(request):
    subprocess.call('cd static/',shell=True)
    subprocess.call('pdflatex texfile',shell=True)
    fs = FileSystemStorage()
    filename = 'texfile.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')

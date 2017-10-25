from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Semester, Course, Exam
from reportlab.pdfgen import canvas
from django.http import HttpResponse, HttpResponseNotFound
from io import BytesIO
from django.db.models import Sum
import os, subprocess
from django.core.files.storage import FileSystemStorage

def home(request):
    u = User.objects.get(username=request.user)
    courses = u.semester_set.get(sem_no=3).course_set.all()
    return render(request, 'performance/home.html', {'courses': courses})

def course_exams(request, pk):
    course = get_object_or_404(Course, pk=pk)
    # items = Exam.objects.all().annotate(Sum('weightage'))
    return render(request, 'performance/exams.html', {'course': course})

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

        #comment = Comment.objects.create(
        #    comment=comment,
        #    exam=exam,

        #)
        exam.save()
        #comment.save()
        return redirect('course_exams', pk=course.pk)
    else:
        return render(request, 'performance/new_exam.html', {'course': course})

def new_course(request):
    if request.method == 'POST':
        name = request.POST['course_name']
        teacher = request.POST['prof']

        user = User.objects.get(username=request.user)  #get the currently logged in user

        course = user.semester_set.get(sem_no=3).course_set.create(
            name=name,
            teacher=teacher,
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
    """
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(300, 500, "Hello world.")
    p.drawString(300, 500, "HBVJHVJGVJKH")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

    response = HttpResponse(content_type='application/pdf')
    #today = date.today()
    filename = 'pdf_demo' #+ today.strftime('%Y-%m-%d')
    response['Content-Disposition'] = 'attachement; filename={0}.pdf'.format(filename)
    buffer = BytesIO()
    report = PdfPrint(buffer, 'A4')
    pdf = report.report(weather_period, 'Weather statistics data')
    response.write(pdf)
    return response
    """
    
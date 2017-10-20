from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Semester, Course, Exam
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import BytesIO

def home(request):
    courses = Course.objects.all()
    return render(request, 'performance/home.html', {'courses': courses})

def course_exams(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'performance/exams.html', {'course': course})

def new_exam(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        name = request.POST['exam'],
        #cond_date = request.POST['cond_date'],
        #weightage = request.POST['weightage'],
        #percentage = request.POST['percentage']

        user = User.objects.first()  #get the currently logged in user

        exam = Exam.objects.create(
            name=name,
            course=course,
            #cond_date=cond_date,
            #weightage=weightage,
            #percentage=percentage,
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
        name = request.POST['subject']

        user = User.objects.first()  #get the currently logged in user

        course = Course.objects.create(
            name=name,
        )

        course.save()
        return redirect('home')
    return render(request, 'performance/new_course.html')

def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

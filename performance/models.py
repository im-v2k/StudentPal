
## @file models.py
#  @author SYNTAX
#  @date 28 Oct 2017
#  
#  @brief This is a file conatining some classes using python.
#
#  It contains of two classes named Course, Exam
#  The arguments describe the type of functions described in the class.

## @package django.db
#  Model fields required for framing custom models are imported from here.
#
from django.db import models
## @package django.contrib.auth.models
#  User model is imported from here.
#
from django.contrib.auth.models import User
## @package django.contrib.core.validators
#  MaxValueValidator,MinValueValidator are imported from here.
#
from django.core.validators import MaxValueValidator, MinValueValidator
## class Course 
#
# maintains data related to courses of user
# name,instructor, exams,code are its parts
#
class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=20, default='')
    name = models.CharField(max_length=50, default='')
    teacher = models.CharField(max_length=50, default='')
    comment = models.TextField(default='')
    ## Used to identify courses by their names.
    #  @return course_code of the Course
    def __str__(self):
        return self.code
    ## Used to get no. of exams in the course
    # 
    #  @return no. of exams in it.
    def get_exams_count(self):
        return Exam.objects.filter(course=self).count()
    ## Used to get exams list as output
    # 
    #  @return list of exams in it.2
    def get_courses(self):
        return list(Exam.objects.filter(course=self))
    ## Used to get percentage in the course
    # 
    #  @return Percentage in the course calculated from exams conducted till now.
    def get_percent_till_now(self):
        if self.get_exams_count() != 0:
            exams = Exam.objects.filter(course=self)
            net_percent = 0
            net_weightage = 0
            for exam in exams:
                net_weightage += exam.weightage
                net_percent += exam.weightage*exam.get_percent()
            ans = (net_percent/net_weightage)
        else:
            ans = 0
        ans = round(ans, 2)
        return ans
    ## Used to get marks in the course
    # 
    #  @return Score in the course calculated from exams conducted till now.
    def get_score_till_now(self):
        if self.get_exams_count() != 0:
            exams = Exam.objects.filter(course=self)
            net_percent = 0
            net_weightage = 0
            for exam in exams:
                net_weightage += exam.weightage
                net_percent += exam.weightage*exam.get_percent()
            ans = (net_percentage)
        else:
            ans = 0
        ans = round(ans, 2)
        return ans
## class Exam 
#
# maintains data related to exams of a course
# name,weighatge,max_marks,marks_obt are its parts
class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30,)
    weightage = models.PositiveSmallIntegerField(default=100)
    max_marks = models.PositiveSmallIntegerField(default=100)
    marks_obt = models.PositiveSmallIntegerField(default=0)
    comment = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name
    ## Used to get percentage of marks
    # 
    #  @return percentage of marks in the exam.
    def get_percent(self):
        percent  = (self.marks_obt/self.max_marks)*100
        percent = round(percent, 2)
        return percent

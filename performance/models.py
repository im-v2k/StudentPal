from django.db import models
#from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=20, default='')
    name = models.CharField(max_length=50, default='')
    teacher = models.CharField(max_length=50, default='')
    comment = models.TextField(default='')

    def __str__(self):
        return self.code
    def get_exams_count(self):
        return Exam.objects.filter(course=self).count()
    def get_courses(self):
        return list(Exam.objects.filter(course=self))

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



class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30,)
    weightage = models.PositiveSmallIntegerField(default=100)
    max_marks = models.PositiveSmallIntegerField(default=100)
    marks_obt = models.PositiveSmallIntegerField(default=0)
    comment = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name

    def get_percent(self):
        percent  = (self.marks_obt/self.max_marks)*100
        percent = round(percent, 2)
        return percent

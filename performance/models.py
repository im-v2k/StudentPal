from django.db import models
#from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
#from userinfo.models import Semester

class Semester(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sem_no = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return "%s's Sem-%s" %(self.user.username, self.sem_no)


class Course(models.Model):
    #user = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    sem = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    course_type = models.CharField(max_length=10,
                                   choices=(('theory', 'Theory'),
                                            ('lab', 'Lab')))
    name = models.CharField(max_length=50, default='')
    description = models.TextField(blank=True, default='')
    course_credits = models.PositiveSmallIntegerField(default=0)
    grade_obt = models.PositiveSmallIntegerField(default=0)
    teacher = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30,)
    max_marks = models.PositiveSmallIntegerField(default=0)
    marks_obt = models.PositiveSmallIntegerField(
        default=0,
        validators=[MaxValueValidator(100, message='No Apsara dark logic please -_-')]
        )
    comment = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name
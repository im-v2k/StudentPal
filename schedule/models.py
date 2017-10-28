## @file models.py
#  @author SYNTAX
#  @date 28 Oct 2017
#  
#  @brief This is a file conatining some classes using python.
#
#  It contains class named Event
#  The arguments describe the type of functions described in the class.

from django.db import models
from django.contrib.auth.models import User

## class Event 
#
# maintains data related to events of user
# name,user,date,description are some of its parts
#
class Event(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=30)
	date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()
	description = models.TextField()
	## Used to identify events by their names.
    #  @return event_name of the Event
	def __str__(self):
		return self.name
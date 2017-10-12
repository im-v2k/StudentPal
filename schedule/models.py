from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=30)
	date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()
	description = models.TextField()

	def __str__(self):
		return self.name
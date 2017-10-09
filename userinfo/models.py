from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from StudentPal import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	dob = models.DateField(blank=True, null=True)
	#dob = models.DateField(blank=True, null=True, input_formats=settings.DATE_INPUT_FORMATS)
	univ = models.CharField(blank=True, max_length=100, default='')
	current_sem = models.PositiveSmallIntegerField(
		default=0,
		validators=[MaxValueValidator(10)]
		)
	gender = models.CharField(
        max_length=20,
		choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('I prefer not to say', 'I prefer not to say')),
        blank=True,
		default='')
	aboutme = models.TextField(blank=True, default='')
	#mobile = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return "%s's profile" %self.user

#	class Meta(User.Meta):
#		pass

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
   	instance.profile.save()

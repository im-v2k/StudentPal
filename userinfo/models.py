from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	dob = models.DateField(blank=True, null=True)
	univ = models.CharField(blank=True, max_length=100)
	gender = models.CharField(
        max_length=1, choices=(('m', _('Male')), ('f', _('Female'))),
        blank=True, null=True)
	aboutme = models.TextField(blank=True, null=True)
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

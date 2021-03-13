from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class Contact(models.Model):
	contact_email 		= models.CharField(max_length=30)
	contact_summary		= models.CharField(max_length=50)
	contact_message 	= models.TextField(max_length=1000)

class Profile(models.Model):
	user 		= models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', primary_key=True)
	user_edit	= models.SlugField(max_length=1000)
	bio			= models.TextField(max_length=120)
	image 		= models.ImageField(default='default.jpg', upload_to='media')
	member 		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def created_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
post_save.connect(created_profile, sender=User)
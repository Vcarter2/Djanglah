from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Contact

class ProfileForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
		'username',
		'email',
		'first_name',
		'last_name',
		'password1',
		'password2',
	]

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'

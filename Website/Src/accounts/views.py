from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

from .forms import ProfileForm, ContactForm
from .models import Profile

User = settings.AUTH_USER_MODEL

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Thank you for your message bitch")
		return redirect('/accounts/contact')
	context = {'form': form}
	return render(request, 'accounts/contact.html', context)

def register(request):
	form = ProfileForm()
	if request.method == 'POST':
		form = ProfileForm(request.POST or None)
		if form.is_valid():
			user = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			form.save()
			return redirect('accounts/login/')
	context = {'form': form}
	return render(request, 'registration/register.html', context)

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('user-username')
		password = request.POST.get('user-password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, 'Good Morning, {}!'.format(request.user))
			return redirect('/accounts/profile/')
	return render(request, 'accounts/login.html', {})

def user_logout(request):
	messages.success(request, "You've logged out successfully!")
	logout(request)
	return redirect('/accounts/login/')

def profile(request):
	return render(request, 'accounts/profile.html', {})

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user'] = timezone.now()
		return context

class ProfileUpdate(UpdateView):
	model = Profile
	form_class = ProfileForm
	template_name = 'accounts/profile_update.html'

	def get_success_url(self):
		return reverse('accounts:profile')

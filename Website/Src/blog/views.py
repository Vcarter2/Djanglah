from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
)

from .models import BlogPost
from .forms import BlogPostForm


class BlogList(ListView):
	model = BlogPost
	template_name = 'blog/blog_list.html'

class BlogDetail(DetailView):
	model = BlogPost
	template_name = 'blog/blog_detail.html'

class BlogCreate(CreateView):
	model = BlogPost
	form_class = BlogPostForm
	template_name = 'blog/blog_create.html'

	def get_success_url(request):
		return reverse('blog:blog-list')

class BlogUpdate(UpdateView):
	model = BlogPost
	form_class = BlogPostForm
	template_name = 'blog/blog_update.html' 

	def get_success_url(request):
		return reverse('blog:blog-list')

class BlogDelete(DeleteView):
	model = BlogPost
	form_class = BlogPostForm
	template_name = 'blog/blog_delete.html' 

	def get_success_url(request):
		return reverse('blog:blog-list')

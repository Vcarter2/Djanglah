from django.db import models
from django.shortcuts import redirect
from django.db.models import Q

class BlogQuerySet(models.query.QuerySet):
	def search(self, query):
		lookups = (
				Q(title__icontains=query) |
				Q(slug__icontains=query)
			)
		return self.filter(lookups).distinct()

class BlogManager(models.Manager):
	def get_queryset(self):
		return BlogQuerySet(self.model, using=self.db)

	def search(self, query):
		return self.get_queryset().search(query)

class BlogPost(models.Model):
	title		= models.CharField(max_length=120)
	slug		= models.SlugField(max_length=120, unique=True)
	image		= models.ImageField(upload_to='media', blank=True)
	content		= models.TextField(max_length=10000)
	timestamp	= models.DateTimeField(auto_now=True)

	objects = BlogManager()

	def __str__(self):
		return self.slug
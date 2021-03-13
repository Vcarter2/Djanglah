from django.shortcuts import render
from django.views.generic import ListView
from django.contrib import messages

from blog.models import BlogPost


class SearchView(ListView):
	template_name = 'search/search_view.html'
	context_object_name = 'searches'

	def get_context_data(self, *args, **kwargs):
		context = super(SearchView, self).get_context_data(*args, **kwargs)
		query = self.request.GET.get('q')
		context['query'] = query
		return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		method_dict = request.GET.query = method_dict.get('q')
		if query is not None:
			return BlogPost.objects.search(query)
		else:
			return BlogPost.objects.none()
		return BlogPost.objects.none()

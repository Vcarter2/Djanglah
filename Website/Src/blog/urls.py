from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
	path('', views.BlogList.as_view(), name='blog-list'),
	path('create/', views.BlogCreate.as_view(), name='blog-create'),
	path('<str:slug>/', views.BlogDetail.as_view(), name='blog-detail'),
	path('<str:slug>/update/', views.BlogUpdate.as_view(), name='blog-update'),
	path('<str:slug>/delete/', views.BlogDelete.as_view(), name='blog-delete'),
]
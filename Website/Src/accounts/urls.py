from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
	path('profile/', views.profile, name='profile'),
	path('contact/', views.contact, name='contact'),
	path('register/', views.register, name='register'),
	path('login/', views.user_login, name='user_login'),
	path('logout/', views.user_logout, name='user_logout'),
	path('profile/<str:id>/update', views.ProfileUpdate.as_view(), name='profile-update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from .import views

urlpatterns = [
	path('load_departments/', views.load_departments, name='load_departments'),
	path('load_sections/', views.load_sections, name='load_sections'),
	path('load_directorates/', views.load_directorates, name="load_directorates"),
]
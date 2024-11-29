# Файл приложения urls.py

from django.urls import path
from .views import about, index, recipe_detail

urlpatterns = [
    path('', index),
    path('recipe/<int:pk>/', recipe_detail),
    path('about/', about),
]
from django.contrib import admin
from django.urls import path

from recipe_project.recipe_app.views import home, create, edit, details, delete

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('details/<int:pk>/', details, name='details'),

]

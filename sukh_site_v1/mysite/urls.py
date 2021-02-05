from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thingsIlike', views.hobbies, name='hobbies'),
    path('projects', views.projects, name='projects'),
    path('calculator', views.calculator, name='calculator')
]
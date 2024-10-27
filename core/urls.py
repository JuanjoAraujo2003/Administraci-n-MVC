from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('project/create/', views.create_project, name='create_project'),
    path('task/create/', views.create_task, name='create_task'),
    path('agregar_empleado/', views.agregar_empleado, name='agregar_empleado'),
]
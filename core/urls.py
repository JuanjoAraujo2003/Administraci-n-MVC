from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import dashboard, create_project, agregar_empleado, create_task
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', login_required(dashboard),name='dashboard'),
    path('project/create/', login_required(create_project), name='create_project'),
    path('task/create/', login_required(create_task), name='create_task'),
    path('core/agregar_empleado/',login_required(agregar_empleado), name='agregar_empleado'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
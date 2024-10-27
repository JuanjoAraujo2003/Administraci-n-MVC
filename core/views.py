from django.shortcuts import render, redirect
from .models import Project, Task, Empleado
from .forms import ProjectForm, TaskForm, EmpleadoForm


def dashboard(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    return render(request, 'core/dashboard.html', {'projects': projects, 'tasks': tasks})

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'core/project_form.html', {'form': form})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'core/task_form.html', {'form': form})

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  
    else:
        form = EmpleadoForm()
    return render(request, 'core/agregar_empleado.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, "Registration successful!")
            return redirect('list')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request,'todo/task_list.html',{'tasks':tasks})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  
            task.user = request.user        
            task.save()
            return redirect('list')
    else:
        form = TaskForm()
    return render(request, 'todo/create.html', {'form': form})

@login_required
def complete(request,task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('list')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user) 
    task.delete()
    return redirect('list')
from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request,'todo/task_list.html',{'tasks':tasks})


def create_task(request):
    if request.method == 'POST':#
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')
    else:
        form = TaskForm()
    return render(request, 'todo/create.html', {'form': form})

def complete(request,task_id):
    instance = Task.objects.get(id =task_id)
    instance.completed = not instance.completed
    instance.save()
    return redirect('list')
# tracker/views.py

from django.shortcuts import render
from .models import Project, Task, TimeLog
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def homepage(request):
    return render(request, 'tracker/homepage.html')
@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'tracker/project_list.html', {'projects': projects})

@login_required
def task_list(request, project_id):
    tasks = Task.objects.filter(project_id=project_id)
    return render(request, 'tracker/task_list.html', {'tasks': tasks})

@login_required
def time_log_list(request, task_id):
    time_logs = TimeLog.objects.filter(task_id=task_id, user=request.user)
    return render(request, 'tracker/time_log_list.html', {'time_logs': time_logs})

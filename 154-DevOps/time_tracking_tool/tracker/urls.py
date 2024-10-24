# tracker/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
    path('tasks/<int:project_id>/', views.task_list, name='task_list'),
    path('time_logs/<int:task_id>/', views.time_log_list, name='time_log_list'),
]

# tracker/admin.py

from django.contrib import admin
from .models import Project, Task, TimeLog

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TimeLog)
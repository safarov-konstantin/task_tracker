from django.contrib import admin
from task_tracker.models import Task, Status


admin.site.register(Task)
admin.site.register(Status)

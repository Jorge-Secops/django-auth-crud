from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", ) #campo de solo lectura que muestra cuando se creo la tarea

admin.site.register(Task, TaskAdmin)

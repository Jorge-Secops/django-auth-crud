from django.db import models
from django.contrib.auth.models import User

# Create your models here. 
#luego hay que registrar las clases en admin.py para poder usarlas en la vista de administrador
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): #con esto retornara en el panel de admin el titulo que le pusimos a la tarea
        return self.title + ' - by ' + self.user.username
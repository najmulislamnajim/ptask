from django.db import models

# Create your models here.
class TaskModel(models.Model):
    taskTitle=models.CharField(max_length=30)
    taskDescription=models.TextField()
    is_completed=models.BooleanField(default=False)
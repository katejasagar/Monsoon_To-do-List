from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class todo_list(models.Model):
    task_name = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
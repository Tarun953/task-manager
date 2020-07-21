from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todos(models.Model):
    completed = models.BooleanField(default=False)
    todotext = models.CharField(max_length=150)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='todo',null=True)

    def __str__(self):
        return self.todotext
    
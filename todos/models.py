from django.db import models

# Create your models here.
class todos(models.Model):
    completed = models.BooleanField(default=False)
    todotext = models.CharField(max_length=150)

    def __str__(self):
        return self.todotext
    
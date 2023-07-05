from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=500)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.content

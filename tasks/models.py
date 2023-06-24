from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
PRIORITY_CHOICES = (
    (1, 'URGENT'),
    (2, 'Normal'),
    (3, 'Low')
)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    due_date = models.DateTimeField()
    attachments = models.FileField(upload_to='/media/')

    class Meta:
        ordering= ['due_date']

    def __Str__(self):
        return f'{self.id} {self.title}'

from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    priority_choices = [
        (1, 'URGENT'),
        (2, 'Normal'),
        (3, 'Low'),
    ]
    status_choices = [
        (1, 'Not Started'),
        (2, 'In Progress'),
        (3, 'Complete'),
        (4, 'On hold'),
    ]
    privacy_choices = [
        (1, "Private"),
        (2, "Public"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    priority = models.IntegerField(choices=priority_choices, default=2)
    due_date = models.DateField(null=True, blank=True)
    privacy = models.IntegerField(choices=privacy_choices, default=1)
    status = models.IntegerField(choices=status_choices, default=1)

    class Meta:
        ordering = ['due_date']
        # this orders the tasks by the closest deadline first

    def __Str__(self):
        return f'{self.id} {self.title}'

from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    priority_choices = [
        (1, 'URGENT'),
        (2, 'Normal'),
        (3, 'Low')
    ]

    def user_directory_path(instance, filename):
        # files will be uploaded to MEDIA_ROOT / user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.owner.id, filename)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    priority = models.IntegerField(choices=priority_choices)
    due_date = models.DateTimeField()
    attachments = models.FileField(
        upload_to=user_directory_path,
        blank=True,
        )

    class Meta:
        ordering= ['due_date']

    def __Str__(self):
        return f'{self.id} {self.title}'

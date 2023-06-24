from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'URGENT'),
        (2, 'Normal'),
        (3, 'Low')
    ]

    def user_directory_path(instance, filename):
        # files will be uploaded to MEDIA_ROOT / user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.user.id, filename)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    due_date = models.DateTimeField()
    attachments = models.FileField(
        upload_to=(upload_to=user_directory_path),
        default='../default_task_j4ryhk',
        blank=True,
        )

    class Meta:
        ordering= ['due_date']

    def __Str__(self):
        return f'{self.id} {self.title}'

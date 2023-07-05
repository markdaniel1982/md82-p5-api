from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from tasks.models import Task


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, unique=True)
    bio = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField(
        upload_to='images/', default='../profileplaceholder_niir6l'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    created_tasks = models.ForeignKey(
        Task, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)

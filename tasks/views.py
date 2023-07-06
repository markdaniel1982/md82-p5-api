from django.http import Http404
from django.db.models import Count
from django.contrib.auth.models import User
from rest_framework import status, generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from taskmonkeyapi.permissions import IsOwnerOrReadOnly


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Task.objects.annotate(
        comments_count=Count('comment', distinct=True)
    ).order_by('due_date')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',
        'status',
        'priority',
        'due_date',
    ]
    search_fields = [
        'owner__username',
        'title',
        'content',
        'status',
        'priority',
        'due_date',
    ]
    ordering_fields = [
        'tasks_count',
        'comments_count',
        'due_date',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.annotate(
        comments_count=Count('comment', distinct=True)
    ).order_by('-due_date')


class PriorityChoices(APIView):
    def get(self):

        priority = Task.priority_choices

        return Response(priority)

from django.http import Http404
from django.db.models import Count
from django.contrib.auth.models import User
from rest_framework import status, generics, permissions, filters
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
        tasks_count=Count('id', distinct=True)
    ).order_by('due_date')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = [
        'owner__username',
        'title',
        'content'
    ]
    ordering_fields = [
        'tasks_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class StatusChoices(APIView):
    def get(self, request, *args, **kwargs):

        status = Task.status_choices

        return Response(status)

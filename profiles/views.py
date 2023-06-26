from django.db.models import Count
from django.http import Http404
from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from taskmonkeyapi.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):

    queryset = Profile.objects.annotate(
        tasks_count=Count('owner__task', distinct=True)
    ).order_by('created_on')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = ['tasks_count']


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

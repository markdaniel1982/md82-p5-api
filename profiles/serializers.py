from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    tasks_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    profile_image = serializers.ImageField()


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'bio',
            'profile_image',
            'created_on',
            'tasks_count',
            'is_owner',
            'comments_count'
        ]

from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'profile_image', 'created_at', 'is_owner']

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.user
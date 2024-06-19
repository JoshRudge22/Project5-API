from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    profile_id = serializers.ReadOnlyField(source='id')
    is_owner = serializers.SerializerMethodField()
    following_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = ['profile_id', 'user', 'full_name', 'bio', 'profile_image', 'created_at', 'is_owner', 'following_count', 'followers_count']

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.user

    def get_following_count(self, obj):
        return obj.user.following.count()

    def get_followers_count(self, obj):
        return obj.user.followers.count()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
from rest_framework import serializers
from .models import Follow
from django.contrib.auth.models import User

class FollowSerializer(serializers.ModelSerializer):
    follower_username = serializers.SerializerMethodField()
    following_username = serializers.SerializerMethodField()

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'follower_username', 'following_username', 'created_at']
        read_only_fields = ['follower']

    def get_follower_username(self, obj):
        return obj.follower.username
    
    def get_following_username(self, obj):
        return obj.following.username

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError("You cannot follow yourself.")
        return data

class FollowerCountSerializer(serializers.ModelSerializer):
    follower_count = serializers.IntegerField(read_only=True)
    following_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'follower_count', 'following_count']
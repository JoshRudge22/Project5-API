from rest_framework import serializers
from .models import Follow
from django.contrib.auth.models import User

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']
        read_only_fields = ['follower']

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError("You cannot follow yourself.")
        return data

class FollowerCountSerializer(serializers.ModelSerializer):
    follower_count = serializers.IntegerField()
    following_count = serializers.IntegerField()

    class Meta:
        model = User
        fields = ['id', 'username', 'follower_count', 'following_count']
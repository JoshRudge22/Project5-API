from rest_framework import serializers
from .models import Like
from posts.models import Post

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post']

class PostLikeSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'likes', 'created_at']

    def get_likes(self, obj):
        return obj.likes.count()
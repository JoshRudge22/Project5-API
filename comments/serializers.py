from rest_framework import serializers
from .models import Comment
from posts.models import Post

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'parent_comment', 'content', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
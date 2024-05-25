from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')

    class Meta:
        model = Post
        fields = ['id', 'user', 'image', 'video', 'caption', 'created_at', 'owner', 'profile_image']
        read_only_fields = ['id', 'user', 'created_at']

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.width > 4096 or value.image.height > 4096:
            raise serializers.ValidationError('Image dimensions larger than 4096px!')
        return value

    def validate_video(self, value):
        if value.size > 1024 * 1024 * 100:
            raise serializers.ValidationError('Video size larger than 100MB!')
        return value
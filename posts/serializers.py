from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'image', 'video', 'caption', 'created_at', 'owner', 'profile_image']
        read_only_fields = ['id', 'user', 'created_at']

    def get_profile_image(self, obj):
        if obj.user.profile.profile_image:
            return obj.user.profile.profile_image.url
        return None

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
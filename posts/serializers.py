from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'image', 'caption', 'created_at', 'owner', 'profile_image']
        read_only_fields = ['id', 'user', 'created_at']

    def get_profile_image(self, obj):
        if obj.user.profile.profile_image:
            return obj.user.profile.profile_image.url
        return None

    def validate(self, data):
        if 'image' not in data or not data['image']:
            raise serializers.ValidationError('You must upload an image')
        if 'image' in data and data['image']:
            if data['image'].size > 10485760:
                raise serializers.ValidationError('Image size should not exceed 10MB')
        return data
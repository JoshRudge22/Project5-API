from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Like
from .serializers import LikeSerializer
from posts.models import Post

class PostLikeView(APIView):
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({'message': 'You already liked this post'}, status=400)
        Like.objects.create(user=request.user, post=post)
        return Response({'message': 'Post liked successfully'})

    def delete(self, request, post_id):
        post = Post.objects.get(id=post_id)
        Like.objects.filter(user=request.user, post=post).delete()
        return Response({'message': 'Post unliked successfully'})

class PostLikesView(APIView):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        likes = post.like_set.all()
        usernames = [like.user.username for like in likes]
        return Response({'usernames': usernames})
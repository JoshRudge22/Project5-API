from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Like
from .serializers import LikeSerializer
from posts.models import Post
from posts.serializers import PostSerializer


class PostLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({'message': 'You already liked this post'}, status=status.HTTP_400_BAD_REQUEST)
        
        Like.objects.create(user=request.user, post=post)
        return Response({'message': 'Post liked successfully'}, status=status.HTTP_200_OK)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like = Like.objects.filter(user=request.user, post=post)
        if like.exists():
            like.delete()
            return Response({'message': 'Post unliked successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)


class PostLikesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        likes = post.like_set.all()
        usernames = [like.user.username for like in likes]
        return Response({'usernames': usernames}, status=status.HTTP_200_OK)


class UserLikedPostsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        liked_posts = Post.objects.filter(like__user=request.user).distinct().order_by('-like__created_at')
        serializer = PostSerializer(liked_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
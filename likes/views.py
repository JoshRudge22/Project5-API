from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from .models import Like
from .serializers import LikeSerializer
from posts.models import Post
from posts.serializers import PostSerializer

class CustomSetPagination(LimitOffsetPagination):
    page_size = 5
    max_page_size = 5

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
    pagination_class = CustomSetPagination

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        likes = post.like_set.all()
        usernames = [like.user.username for like in likes]
        return Response({'usernames': usernames})

class UserLikedPostsView(APIView):
    pagination_class = CustomSetPagination

    def get(self, request):
        likes = Like.objects.filter(user=request.user)
        liked_posts = [like.post for like in likes]
        serializer = PostSerializer(liked_posts, many=True)
        return Response(serializer.data)
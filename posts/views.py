from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import Http404
from .models import Post
from follow.models import Follow
from .serializers import PostSerializer
from api.permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(user=self.request.user).order_by('-created_at')
        else:
            return Post.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetail(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserPostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

class FeedList(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

    def get_queryset(self):
        limit = int(self.request.GET.get('limit', 5))
        offset = int(self.request.GET.get('offset', 0))
        posts = Post.objects.all().order_by('-created_at')[offset:offset + limit]
        has_more_posts = Post.objects.count() > offset + limit
        return posts, has_more_posts

    def list(self, request, *args, **kwargs):
        queryset, has_more_posts = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'posts': serializer.data, 'has_more_posts': has_more_posts})

class FollowingFeed(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        following_users = Follow.objects.filter(follower=request.user).values_list('following', flat=True)
        limit = int(self.request.GET.get('limit', 5))
        offset = int(self.request.GET.get('offset', 0))
        following_posts = Post.objects.filter(user__in=following_users).order_by('-created_at')[offset:offset + limit]
        serializer = PostSerializer(following_posts, many=True)
        has_more_posts = Post.objects.filter(user__in=following_users).count
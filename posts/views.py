from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from follow.models import Follow
from .serializers import PostSerializer
from api.permissions import IsOwnerOrReadOnly

class CustomSetPagination(LimitOffsetPagination):
    page_size = 5
    max_page_size = 5

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination

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
    pagination_class = CustomSetPagination

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by('-created_at')

class AllUserPostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = CustomSetPagination

    def get_queryset(self):
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)
        return Post.objects.filter(user=user).order_by('-created_at')

class FeedList(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    pagination_class = CustomSetPagination
    

class FollowingFeed(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomSetPagination

    def get(self, request):
        following_users = Follow.objects.filter(follower=request.user).values_list('following', flat=True)
        following_posts = Post.objects.filter(user__in=following_users).order_by('-created_at')
        paginator = CustomSetPagination()
        paginated_following_posts = paginator.paginate_queryset(following_posts, request)
        serializer = PostSerializer(paginated_following_posts, many=True)
        return paginator.get_paginated_response(serializer.data)

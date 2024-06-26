from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from django.http import Http404
from .models import Follow
from .serializers import FollowSerializer, FollowerCountSerializer
from django.contrib.auth.models import User
from django.db.models import Count

class FollowUser(APIView):
    def post(self, request, username):
        following_user = User.objects.get(username=username)
        follow, created = Follow.objects.get_or_create(follower=request.user, following=following_user)
        if created:
            return Response({'message': 'You are now following this user.'}, status=201)
        return Response({'message': 'You are already following this user.'}, status=200)

class UnfollowUser(APIView):
    def delete(self, request, username):
        following_user = User.objects.get(username=username)
        try:
            Follow.objects.get(follower=request.user, following=following_user).delete()
            return Response({'message': 'You are no longer following this user.'}, status=204)
        except Follow.DoesNotExist:
            return Response({'message': 'You are not following this user.'}, status=404)

class FollowersList(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        username = self.kwargs['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        return Follow.objects.filter(following=user)

class FollowingList(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        username = self.kwargs['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        return Follow.objects.filter(follower=user)

class FollowerCountView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = FollowerCountSerializer
    lookup_field = 'username'

    def get_object(self):
        user = super().get_object()
        user.follower_count = user.followers.count()
        user.following_count = user.following.count()
        return user

class FollowingCountView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = FollowerCountSerializer
    lookup_field = 'username'

    def get_object(self):
        user = super().get_object()
        user.follower_count = user.followers.count()
        user.following_count = user.following.count()
        return user

class IsFollowing(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, username):
        try:
            following_user = User.objects.get(username=username)
            is_following = Follow.objects.filter(follower=request.user, following=following_user).exists()
            return Response({'is_following': is_following}, status=200)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
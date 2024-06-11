from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.http import Http404
from .models import Follow
from .serializers import FollowSerializer, FollowerCountSerializer
from django.contrib.auth.models import User
from django.db.models import Count

class FollowUser(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)

class UnfollowUser(generics.DestroyAPIView):
    queryset = Follow.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        following_user = self.kwargs['following_id']
        try:
            return Follow.objects.get(follower=self.request.user, following__id=following_user)
        except Follow.DoesNotExist:
            raise Http404

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

class FollowerFollowingCount(generics.RetrieveAPIView):
    queryset = User.objects.annotate(
        follower_count=Count('followers'),
        following_count=Count('following')
    )
    serializer_class = FollowerCountSerializer
    lookup_field = 'username'
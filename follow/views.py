from rest_framework import generics, permissions
from api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer

class FollowerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)

class FollowerDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

class UserFollowersList(generics.ListAPIView):
    serializer_class = FollowerSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Follower.objects.filter(user_id=user_id)

class UserFollowingList(generics.ListAPIView):
    serializer_class = FollowerSerializer

    def get_queryset(self):
        follower_id = self.kwargs['user_id']
        return Follower.objects.filter(follower_id=follower_id)
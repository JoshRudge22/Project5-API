from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Like
from .serializers import LikeSerializer

class LikeCreateAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class LikeListAPIView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
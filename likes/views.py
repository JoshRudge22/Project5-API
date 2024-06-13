from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Like
from .serializers import LikeSerializer
from rest_framework.response import Response
from django.db.models import Count

class LikeCreateAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class LikeListAPIView(generics.ListAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        comment_id = self.kwargs.get('comment_id')
        if post_id:
            return Like.objects.filter(post_id=post_id)
        elif comment_id:
            return Like.objects.filter(comment_id=comment_id)
        return Like.objects.none()

class LikeCountAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        post_id = self.kwargs.get('post_id')
        comment_id = self.kwargs.get('comment_id')
        if post_id:
            count = Like.objects.filter(post_id=post_id).count()
        elif comment_id:
            count = Like.objects.filter(comment_id=comment_id).count()
        else:
            count = 0
        return Response({'count': count})
from rest_framework import generics
from .models import FeedItem
from .serializers import FeedItemSerializer

class FeedList(generics.ListAPIView):
    queryset = FeedItem.objects.all().order_by('-created_at')
    serializer_class = FeedItemSerializer
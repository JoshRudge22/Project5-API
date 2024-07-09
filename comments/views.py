from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from .models import Comment
from posts.models import Post
from .serializers import CommentSerializer
from posts.serializers import PostSerializer
from api.permissions import IsOwnerOrReadOnly

class CustomSetPagination(LimitOffsetPagination):
    page_size = 5
    max_page_size = 5

class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id, parent_comment__isnull=True).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, post_id=self.kwargs['post_id'])

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class UserCommentedPostsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomSetPagination

    def get(self, request):
        user_id = request.user.id
        commented_posts = Post.objects.filter(comments__user_id=user_id).order_by('-comments__created_at')
        pagination_class = CustomSetPagination()
        paginated_queryset = pagination_class.paginate_queryset(commented_posts, request)
        serializer = PostSerializer(paginated_queryset, many=True)
        return pagination_class.get_paginated_response(serializer.data)
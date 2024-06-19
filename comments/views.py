from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment
from posts.models import Post
from .serializers import CommentSerializer
from posts.serializers import PostSerializer
from api.permissions import IsOwnerOrReadOnly

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

    def get(self, request, pk):
        user_id = request.user.id
        commented_posts = Post.objects.filter(comments__user_id=user_id).distinct()
        serializer = PostSerializer(commented_posts, many=True)
        return Response(serializer.data)
from django.urls import path
from comments import views

urlpatterns = [
    path('posts/<int:post_id>/comments/', views.CommentListCreateAPIView.as_view()),
    path('comments/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('comments/user/<int:pk>/', views.UserCommentedPostsAPIView.as_view()),
]
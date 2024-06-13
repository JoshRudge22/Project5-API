from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.LikeCreateAPIView.as_view()),
    path('likes/posts/<int:post_id>/', views.LikeListAPIView.as_view()),
    path('likes/comments/<int:comment_id>/', views.LikeListAPIView.as_view()),
    path('likes/posts/<int:post_id>/count/', views.LikeCountAPIView.as_view()),
    path('likes/comments/<int:comment_id>/count/', views.LikeCountAPIView.as_view()),
]
from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('feed/', views.FeedList.as_view()),
    path('posts/user/', views.UserPostList.as_view()),
    path('feed/following', views.FollowingFeed.as_view())
]
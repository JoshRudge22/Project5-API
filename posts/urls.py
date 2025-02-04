from django.urls import path, include
from posts import views

urlpatterns = [
    path("posts/", views.PostList.as_view()),
    path("posts/<int:pk>/", views.PostDetail.as_view()),
    path("feed/", views.FeedList.as_view(), name="feed"),
    path("posts/user/", views.UserPostList.as_view()),
    path("feed/following/", views.FollowingFeed.as_view()),
    path("user/<str:username>/posts/", views.AllUserPostList.as_view()),
]
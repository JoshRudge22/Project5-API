from django.urls import path
from. import views

urlpatterns = [
    path('profiles/<str:username>/follow/', views.FollowUser.as_view()),
    path('profiles/<str:username>/unfollow/', views.UnfollowUser.as_view()),
]
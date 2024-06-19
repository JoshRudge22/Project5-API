from django.urls import path
from. import views

urlpatterns = [
    path('profiles/<str:username>/follow/', views.FollowUser.as_view()),
    path('profiles/<str:username>/unfollow/', views.UnfollowUser.as_view()),
    path('followers/<str:username>/', views.FollowersList.as_view()),
    path('following/<str:username>/', views.FollowingList.as_view()),
]
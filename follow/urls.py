from django.urls import path
from follow import views

urlpatterns = [
    path('followers/', views.FollowUser.as_view()),
    path('unfollow/<int:following_id>/', views.UnfollowUser.as_view()),
    path('followers/<str:username>/', views.FollowersList.as_view()),
    path('following/<str:username>/', views.FollowingList.as_view()),
    path('counts/<str:username>/', views.FollowerFollowingCount.as_view()),
]
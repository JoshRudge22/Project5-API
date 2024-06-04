from django.urls import path
from follow import views

urlpatterns = [
    path('followers/', views.FollowerList.as_view()),
    path('followers/<int:pk>/', views.FollowerDetail.as_view()),
    path('user/<int:user_id>/followers/', views.UserFollowersList.as_view()),
    path('user/<int:user_id>/following/', views.UserFollowingList.as_view()),
]
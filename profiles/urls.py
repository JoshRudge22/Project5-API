from django.urls import path, include
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/update/<int:pk>/', views.ProfileDetail.as_view()),
    path('profiles/<str:username>/', views.UserProfileViewByUsername.as_view()),
    path('profiles/delete/<str:username>/', views.DeleteProfileView.as_view()),
]
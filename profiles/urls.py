from django.urls import path
from .views import ProfileList, ProfileDetail, UserProfileViewByUsername, DeleteProfileView

urlpatterns = [
    path('', ProfileList.as_view(), name='profile-list'),
    path('<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('username/<str:username>/', UserProfileViewByUsername.as_view(), name='profile-by-username'),
    path('delete/<str:username>/', DeleteProfileView.as_view(), name='profile-delete'),
]
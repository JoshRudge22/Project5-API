from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.LikeCreateAPIView.as_view()),
    path('likes/<int:post_id>/', views.LikeListAPIView.as_view()),
]
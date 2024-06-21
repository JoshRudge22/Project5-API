from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:post_id>/like/', views.PostLikeView.as_view()),
    path('posts/<int:post_id>/likes/', views.PostLikesView.as_view()),
]
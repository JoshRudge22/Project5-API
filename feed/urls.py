from django.urls import path
from feed import views

urlpatterns = [
    path('feed/', views.FeedList.as_view()),
]
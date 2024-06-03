from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_followers')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_users')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'follower']
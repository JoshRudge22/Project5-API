from django.db import models
from django.contrib.auth.models import User

class FeedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feed Item {self.id}'

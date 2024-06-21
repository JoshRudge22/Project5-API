from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Like by {self.user.username} on post {self.post.id}"
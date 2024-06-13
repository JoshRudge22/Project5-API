from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'post', 'comment']

    def __str__(self):
        return f"{self.user.username} liked {'post' if self.post else 'comment'}"
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='default_post_saobzq.jpg', blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.caption[:20]}'

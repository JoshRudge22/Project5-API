from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=60)
    number = models.CharField(max_length=15, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name
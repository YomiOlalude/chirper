from django.db import models
from django.conf import settings


# Create your models here.

# User = settings.AUTH_USER_MODEL

class Chirp(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=280, blank=False)
    image = models.FileField(null=True, blank=True)
    # time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ["-id"]

    

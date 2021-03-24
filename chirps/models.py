from django.db import models
from django.conf import settings


# Create your models here.

User = settings.AUTH_USER_MODEL

class ChirpLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chirp = models.ForeignKey("Chirp", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Chirp(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=280, blank=False)
    likes = models.ManyToManyField(User, related_name="chirp_user", blank=True, through=ChirpLike)
    image = models.FileField(upload_to="images/", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ["-id"]

    

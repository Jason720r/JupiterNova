from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)
    alignment = models.ForeignKey("Alignment", on_delete=models.CASCADE, related_title="alignment")
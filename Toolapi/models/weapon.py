from django.db import models
from django.contrib.auth.models import User

class Weapons(models.Model):
    title = models.CharField(max_length=20)
    damage = models.CharField(max_length=40)
    rarity = models.ForeignKey("Rarity", on_delete=models.CASCADE, related_name="rarity")
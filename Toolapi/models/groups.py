from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    Name = models.CharField(max_length=100)
    alignment = models.ForeignKey("Alignment", on_delete=models.CASCADE, related_name="alignment")

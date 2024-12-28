from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    Name = models.Charfield(max_length=100)
    aalignment = models.ForeignKey("Alignment", on_delete=models.CASCADE, related_title="alignment")

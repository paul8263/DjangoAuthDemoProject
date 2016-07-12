from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class DEUserProfile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=100, blank=True)


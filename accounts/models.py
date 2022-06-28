from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class ProfileImage(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
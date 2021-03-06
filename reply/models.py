from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from board.models import Post
from accounts.models import User

class Reply(models.Model):
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='reply_likes', blank=True)

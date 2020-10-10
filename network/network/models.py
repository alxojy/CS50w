from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following") # user following
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower") # user with follower

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user") 
    post = models.CharField(max_length=300) # text post
    timestamp = models.DateTimeField()
    likes = models.IntegerField(default=0)

    def serialize(self):
        return {
            "likes":self.likes
        }

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likeduser") 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likedpost") 
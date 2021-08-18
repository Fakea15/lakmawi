from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# database
class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False, upload_to='images/')
    description = models.TextField(max_length=300)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

class Message(models.Model):
    sender = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.sender

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=False, blank=False, upload_to='images/profile/')
    facebook_url = models.CharField(max_length=30, null=True, blank=True)
    twitter_url = models.CharField(max_length=30, null=True, blank=True)
    instagram_url = models.CharField(max_length=30, null=True, blank=True)


    def __str__(self):
        return str(self.user)



from django.db import models
from accounts.models import UserAccount


class Post(models.Model):
    host = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
    description = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Comment(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    body = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body



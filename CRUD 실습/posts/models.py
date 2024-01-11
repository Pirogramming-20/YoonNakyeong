from django.db import models

class Post(models.Model) :
    title=models.CharField(max_length=32)
    user=models.CharField(max_length=32)
    content=models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content=models.TextField()
# Create your models here.

# id, title, user, content
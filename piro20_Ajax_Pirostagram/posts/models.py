from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField('제목',max_length=24)
    content=models.TextField('내용')
    like = models.IntegerField()
    image=models.ImageField('Image', blank=False)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment=models.TextField()
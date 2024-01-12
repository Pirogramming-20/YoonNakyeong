from django.db import models

# Create your models here.
# id, 영화 제목, 개봉 년도, 장르, 별점

class Review(models.Model):
    title=models.CharField(max_length=32)
    year=models.IntegerField()
    genre=models.CharField(max_length=32)
    rating=models.DecimalField(max_digits=2, decimal_places=1)
    director=models.CharField(max_length=32)
    character=models.CharField(max_length=32)
    time=models.IntegerField()
    story=models.TextField()
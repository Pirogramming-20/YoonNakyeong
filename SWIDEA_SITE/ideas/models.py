from django.db import models

# Create your models here.
class Idea(models.Model):
    title=models.CharField('아이디어명', max_length=24)
    image=models.ImageField('Image', blank=False)
    content=models.CharField('아이디어 설명', max_length=1000)
    interest=models.IntegerField('아이디어 관심도', default=1)
    devtool=models.CharField('예상 개발 툴', max_length=24)
    
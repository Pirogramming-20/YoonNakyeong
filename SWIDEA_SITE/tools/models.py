from django.db import models

# Create your models here.
class Tool(models.Model):
    name=models.CharField('이름', max_length=24)
    kind=models.CharField('종류', max_length=24)
    content=models.CharField('개발툴 설명', max_length=1000)
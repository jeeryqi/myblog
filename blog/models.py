from django.db import models
from django.conf import settings


# Create your models here.

class BlogType(models.Model):
    type_name = models.CharField('博客类型', max_length=20)
    ordering = 'pk'

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField('标题', max_length=50)
    content = models.TextField('内容')
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs', verbose_name='作者')
    create_time = models.DateTimeField('发布时间', auto_now_add=True)
    last_update_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.title

from django.db import models
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User


# Create your models here.

class BlogType(models.Model):
    type_name = models.CharField('博客类型', max_length=20)

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ('pk')


class Blog(models.Model):
    blog_type = models.ForeignKey(to=BlogType, on_delete=models.CASCADE, related_name='blogs', default=1)
    title = models.CharField('标题', max_length=50)
    content = models.TextField('内容')
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs',
                               verbose_name='作者', default=1)
    create_time = models.DateTimeField('发布时间', auto_now_add=True)
    last_update_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.title

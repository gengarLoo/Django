from django.db import models

# Create your models here.

class Article(models.Model):
    # 文章的唯一Id
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章摘要
    brief_content = models.TextField()
    # 文章内容
    content = models.TextField()
    # 文章发布时间
    date = models.DateTimeField(auto_now=True)

    # 在页面返回文章标题
    def  __str__(self):
        return self.title
    
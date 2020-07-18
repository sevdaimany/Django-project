from django.db import models


class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug =models.SlugField()
    body =models.TextField()
    date =models.DateTimeField(auto_now_add = True)

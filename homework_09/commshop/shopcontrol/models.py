from django.db import models


# Create your models here.
class News(models.Model):
    name = models.CharField(verbose_name='news_name', max_length=100)
    date = models.DateField(verbose_name='news_date')
    text = models.TextField(verbose_name='news_text', blank=True)
    actual = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=100)

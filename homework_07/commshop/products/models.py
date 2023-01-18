from django.db import models
"""
This products models are based on EAV model (https://en.wikipedia.org/wiki/Entity%E2%80%93attribute%E2%80%93value_model)
"""


# Create your models here.
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=50, unique=True)


class ProductInstance(models.Model):
    name = models.CharField(verbose_name='name', max_length=50, unique=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)


class PropertyType(models.Model):
    name = models.CharField(verbose_name='name', max_length=50, unique=True)
    type = models.CharField(verbose_name='type', max_length=20)
    prod_cat = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)


class PropertyInstance(models.Model):
    value = models.CharField(verbose_name='value', max_length=20)
    text_value = models.TextField(verbose_name='text_value', blank=True)
    prod_inst = models.ForeignKey(ProductInstance, on_delete=models.PROTECT)
    prod_type = models.ForeignKey(PropertyType, on_delete=models.PROTECT)

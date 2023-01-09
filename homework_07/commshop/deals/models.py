from django.db import models
from products.models import ProductInstance


def increment_product_code_number():
    last_product_record = ProductElement.objects.all().order_by('id').last()
    old_code_number = last_product_record.code_number
    new_code_number = int(old_code_number) + 1
    return new_code_number


# Create your models here.
class Committent(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    registration_date = models.DateField(verbose_name='registration_date', auto_now=True)


class DealStatus(models.Model):
    status_text = models.CharField(max_length=50, unique=True)


class Deal(models.Model):
    committent = models.ForeignKey(Committent, on_delete=models.PROTECT)
    commission = models.IntegerField(verbose_name='commission', default=12)
    date_start = models.DateField(verbose_name='deal_date_start', auto_now=True)
    date_close = models.DateField(verbose_name='deal_date_close')
    status = models.ForeignKey(DealStatus, on_delete=models.PROTECT)


class ProductElement(models.Model):
    prod_inst = models.ForeignKey(ProductInstance, on_delete=models.PROTECT)
    deal = models.ForeignKey(Deal, on_delete=models.PROTECT)
    code_number = models.CharField(max_length=7, default=increment_product_code_number, editable=False)
    price = models.IntegerField(verbose_name='price')
    amount = models.IntegerField(verbose_name='amount', default=1)
    notes = models.TextField(verbose_name='notes', blank=True)

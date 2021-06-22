from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

class product(models.Model):
    prod_name = models.CharField(max_length=16,primary_key=True)
    Sell_price =models.FloatField()
    buy_price = models.FloatField()
    prod_category = models.CharField(max_length=16)
    number_of_units = models.FloatField
    date_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.prod_name)

class cash_sales(models.Model):
    trans_id = models.AutoField(primary_key=True)
    prod_name = models.ForeignKey(product, on_delete='CASCADE')
    prod_quantity = models.FloatField()
    prod_unit_price =models.FloatField()
    total_price = models.FloatField()
    trans_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.prod_name)


class category(models.Model):
    categ_id = models.AutoField(primary_key=True)
    Categ_name = models.CharField(max_length=16)
    Categ_desc = models.CharField(max_length=120)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Categ_name)

class  credited_customer(models.Model):
    cust_contact = models.IntegerField(primary_key=True)
    cust_id = models.IntegerField()
    fname =models.CharField(max_length=16)
    lname =models.CharField(max_length=16)
    address = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.fname)

class credits(models.Model):
    prod_name = models.ForeignKey(product,primary_key=True, on_delete='CASCADE')
    prod_quantity = models.IntegerField()
    total_price = models.IntegerField()
    cust_contact =models.ForeignKey(credited_customer,on_delete='CASCADE')
    due_date = models.DateTimeField()
    date_credited = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.prod_name)

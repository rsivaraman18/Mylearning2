from django.db import models
from Products.models import *

class MyCustomer(models.Model):
    Customer_name = models.CharField(max_length=35,null=True)
    Customer_since = models.DateField(null=True)
    Customer_location = models.CharField(max_length=50)

    def __str__(self):
        return self.Customer_name


class Myorders(models.Model):
    customer_reference = models.ForeignKey(MyCustomer, on_delete=models.CASCADE , null=True)
    product_reference  = models.ForeignKey(MyProducts, on_delete=models.SET_NULL, null=True)
    order_number       = models.CharField(max_length=20 , null= True)
    order_date         = models.DateField(null=True)
    quantity           = models.FloatField(default=0)
    amount             = models.FloatField(default=0)
    gst_number         = models.FloatField(default=0)
    bill_amount        = models.FloatField(default=0)

    def __str__(self):
        return f'{self.order_number} - Amount Rs {self.amount}'
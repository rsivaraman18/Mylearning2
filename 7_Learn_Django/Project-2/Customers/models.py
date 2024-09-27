from django.db import models


class MyCustomer(models.Model):
    Customer_name = models.CharField(max_length=35,null=True)
    Customer_since = models.DateField(null=True)
    Customer_location = models.CharField(max_length=50)

    def __str__(self):
        return self.Customer_name



from django.db import models

class MyProducts(models.Model):
    product_name = models.CharField(max_length=35,null=True)
    product_code = models.CharField(max_length=35,null=True)
    product_price = models.FloatField(default=0)
    product_gst  = models.IntegerField(default=0)
    food_product = models.BooleanField(default=0)


    def __str__(self):
        return f"{self.product_name}  {self.product_price}"

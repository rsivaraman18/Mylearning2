from django.forms import ModelForm
from .models import *


class MyCustomerForm(ModelForm):
    class Meta:
        model = MyCustomer
        fields = '__all__'


class MyOrderForm(ModelForm):
    class Meta:
        model = Myorders
        # fields = '__all__'
        fields = ['customer_reference','product_reference','order_number','order_date','quantity']



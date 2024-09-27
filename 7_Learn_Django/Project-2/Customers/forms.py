from django.forms import ModelForm
from .models import *


class MyCustomerForm(models.Model):
    class meta:
        model = MyCustomer
        fields = '__all__'

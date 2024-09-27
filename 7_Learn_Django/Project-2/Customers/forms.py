from django.forms import ModelForm
from .models import *


class MyCustomerForm(ModelForm):
    class Meta:
        model = MyCustomer
        fields = '__all__'




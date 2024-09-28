from django.forms import ModelForm
from .models import *


class MyProductForm(ModelForm):
    class Meta:
        model = MyProducts
        fields = '__all__'




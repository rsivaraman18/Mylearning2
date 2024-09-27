from django.forms import ModelForm
from .models import *

class StudentMyform(ModelForm):

    class Meta:

        model = Mystudent
        fields = "__all__"
## Employee

from django.urls import path
from . import views

urlpatterns = [
    path('greet/' ,views.greet),
    path('viewall/',views.viewall)
]
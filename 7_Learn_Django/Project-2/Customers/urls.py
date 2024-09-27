

from django.urls import path
from .import views


urlpatterns = [
    path('customer_add/',     views.CustomerAdd),
    path('customer_viewall/', views.CustomerViewall , name='customerlist'),
    path('customer_delete/<int:id>/',  views.CustomerDelete),
    path('customer_update/<int:id>/',  views.CustomerUpdate),
]

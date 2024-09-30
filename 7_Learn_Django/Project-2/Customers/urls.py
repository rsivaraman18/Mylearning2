

from django.urls import path
from .import views


urlpatterns = [
    path('customer_add/',     views.CustomerAdd),
    path('customer_viewall/', views.CustomerViewall , name='customerlist'),
    path('customer_delete/<int:id>/',  views.CustomerDelete),
    path('customer_update/<int:id>/',  views.CustomerUpdate),

    
    path('customer_vieworders/',  views.CustomerViewOrder , name='orderslist'),
    path('customer_neworder/',   views.CustomerNewOrder),
    path('customer_orderdelete/<int:id>/',   views.CustomerOrderDelete),
    path('customer_orderupdate/<int:id>/',   views.CustomerOrderUpdate),

]

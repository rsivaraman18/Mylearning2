from django.urls import path
from .import views

urlpatterns = [
    path('product_add/',     views.ProductAdd),
    path('product_viewall/', views.ProductViewall , name='productlist'),
    path('product_delete/<int:id>/',  views.ProductDelete),
    path('product_update/<int:id>/',  views.ProductUpdate),
]

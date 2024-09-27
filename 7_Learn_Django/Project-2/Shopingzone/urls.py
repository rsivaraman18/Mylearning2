
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Customers/', include('Customers.urls')),
    path('Products/',  include('Products.urls')),
    path('', views.main_home),
]

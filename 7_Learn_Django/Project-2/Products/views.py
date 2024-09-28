from django.shortcuts import render,redirect
from Products. models import *
from django.contrib import messages
from . forms import *

"""Here Everything Done with Dual Method"""

def ProductAdd(request):
    prod_form = MyProductForm()
    if request.method == 'POST':
        """Method 1"""
        product_name  = request.POST['product_name']
        product_code  = request.POST['product_code']
        product_price = request.POST['product_price']
        product_gst   = request.POST['product_gst']
        food_product  = request.POST['food_product']
        newproduct    = MyProducts(product_name=product_name,product_code=product_code,product_price=product_price,product_gst=product_gst,food_product=food_product)
        newproduct.save()
        return redirect('productlist')
    return render(request,'Product/1_add.html',{'prod_form':prod_form})


def ProductAdd(request):
    prod_form = MyProductForm()
    if request.method == 'POST':
        """Method 2- Using Form """
        newproduct = MyProductForm(request.POST)
        newproduct.save()
        return redirect('productlist')
    return render(request,'Product/1_add.html',{'prod_form':prod_form})



def ProductViewall(request):
    allproducts = MyProducts.objects.all()
    datas = {'datas':allproducts}
    return render(request,'Product/2_viewall.html',datas)



def ProductDelete(request,id):
    productdetail = MyProducts.objects.get(id=id)
    productdetail.delete()
    messages.success(request,f'Product {productdetail.product_name} ID{id} Deleted')
    return redirect('productlist')


def ProductUpdate(request,id):
    prod_oldinfo = MyProducts.objects.get(id=id)
    prod_form    = MyProductForm(instance=prod_oldinfo)
    if request.method=='POST':
        update_prod = MyProductForm(request.POST,instance=prod_oldinfo)
        if update_prod.is_valid():
            update_prod.save()
            messages.success(request,'Updated Successfully')
        else:
            messages.warning(request,update_prod.errors)
        return redirect('productlist')
    
    return render(request,'Product/3_update.html',{'prod_form':prod_form})

    
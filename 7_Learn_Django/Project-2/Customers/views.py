from django.shortcuts import render,redirect
from Customers. models import *
from django.contrib import messages
from . forms import *

"""Here Everything Done with Dual Method"""

def CustomerAdd(request):
    cust_form = MyCustomerForm()
    if request.method == 'POST':
        """Method 1"""
        cname     = request.POST['Customer_name']
        csince    = request.POST['Customer_since']
        clocation = request.POST['Customer_location']
        newcustomer = MyCustomer(Customer_name=cname,Customer_since=csince,Customer_location=clocation,)
        newcustomer.save()
        return redirect('/Customers/customer_viewall/')
    return render(request,'Customer/1_add.html',{'cust_form':cust_form})


def CustomerAdd(request):
    cust_form = MyCustomerForm()
    if request.method == 'POST':
        """Method 2- Using Form """
        newcustomer = MyCustomerForm(request.POST)
        newcustomer.save()
        return redirect('/Customers/customer_viewall/')
    return render(request,'Customer/1_add.html',{'cust_form':cust_form})


def CustomerViewall(request):
    allcustomers = MyCustomer.objects.all()
    datas = {'datas':allcustomers}
    return render(request,'Customer/2_viewall.html',datas)


def CustomerDelete(request,id):
    customerdetail = MyCustomer.objects.get(id=id)
    customerdetail.delete()
    messages.success(request,f'Customer {customerdetail.Customer_name} ID{id} Deleted')
    return redirect('/Customers/customer_viewall/')


def CustomerUpdate(request,id):
    cust_oldinfo = MyCustomer.objects.get(id=id)
    cust_form    = MyCustomerForm(instance=cust_oldinfo)
    if request.method=='POST':
        update_cust = MyCustomerForm(request.POST,instance=cust_oldinfo)
        if update_cust.is_valid():
            update_cust.save()
            messages.success(request,'Updated Successfully')
        else:
            messages.warning(request,update_cust.errors)
        return redirect('customerlist')
    
    return render(request,'Customer/3_update.html',{'cust_form':cust_form})

from datetime import * 

def CustomerNewOrder(request):
    order_form = MyOrderForm()
    context = {'cust_order_form':order_form}
    if request.method=='POST':
        productid        = request.POST['product_reference']
        customerid       = request.POST['customer_reference']
        selected_product = MyProducts.objects.get(id=productid)
        customer_name    = MyCustomer.objects.get(id=customerid)
        ## Date Formating
        order_date_str   = request.POST['order_date']
        forder_date      = datetime.strptime(order_date_str, '%d-%b-%Y').date()
        ## Calculation
        amount           = float(selected_product.product_price) * float(request.POST['quantity'])
        gst_amount       = (amount * selected_product.product_gst)/100
        bill_amount      = amount + gst_amount
        
        neworder = Myorders(customer_reference = customer_name,
                            product_reference  = selected_product,
                            order_number       = request.POST['order_number'],
                            order_date         = forder_date,
                            quantity           = request.POST['quantity'],
                            amount             = amount,
                            gst_number         = gst_amount,
                            bill_amount        = bill_amount,
                            )
        
        neworder.save()
        messages.success(request,"New Order Placed Successfully")
        return redirect('orderslist')
    
    return render(request,'Customer/4_orderpage.html',context)



def CustomerViewOrder(request):
    allorders = Myorders.objects.all()
    datas = {'datas':allorders}
    return render(request,'Customer/5_orderview.html',datas)



def CustomerOrderDelete(request,id):
    order = Myorders.objects.get(id=id)
    order.delete()
    messages.success(request,f'Order Id{id} deleted Successfully')
    return redirect('orderslist')


def CustomerOrderUpdate(request,id):
    order     = Myorders.objects.get(id=id)
    orderform = MyOrderForm(instance=order)
    context   = {'order_updateform':orderform}
    if request.method == 'POST':
        productid        = request.POST['product_reference']
        customerid       = request.POST['customer_reference']
        selected_product = MyProducts.objects.get(id=productid)
        customer_name    = MyCustomer.objects.get(id=customerid)
        ## Date Formating
        order_date_str   = request.POST['order_date']
        forder_date      = datetime.strptime(order_date_str, '%d-%b-%Y').date()
        ## Calculation
        amount           = float(selected_product.product_price) * float(request.POST['quantity'])
        gst_amount       = (amount * selected_product.product_gst)/100
        bill_amount      = amount + gst_amount
        
        neworder = Myorders(customer_reference = customer_name,
                            product_reference  = selected_product,
                            order_number       = request.POST['order_number'],
                            order_date         = forder_date,
                            quantity           = request.POST['quantity'],
                            amount             = amount,
                            gst_number         = gst_amount,
                            bill_amount        = bill_amount,
                            )
        
        neworder.save()
        messages.success(request,"Order Updated Successfully")
        return redirect('orderslist')
    return render(request , 'Customer/6_orderupdate.html',context)
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

    
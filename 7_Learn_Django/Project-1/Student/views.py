from django.shortcuts import render,redirect
from django.http import HttpResponse

def greet(request):
    return HttpResponse('Welcome to Django')


def index_page(request):
    return render(request,'index.html')

def index_page2(request):
    return render(request,'index2.html')


from .models import *
from .forms import *

def student_register(request):
    if request.method=="POST":
       new_student =  StudentMyform(request.POST)
       if new_student.is_valid():
           new_student.save()

    context = {'studentform':StudentMyform()}
    return render(request,'studentregister.html',context)

# Aliter Method
def student_register(request):
    if request.method=="POST":
        uname   = request.POST['name']
        udesign = request.POST['designation']
        upay    = request.POST['pay']

        new_student = Mystudent(name=uname, designation=udesign, pay=upay)
        new_student.save()

    context = {'studentform':StudentMyform()}
    return render(request,'studentregister.html',context)


def Student_viewall(request):
    allstudent = Mystudent.objects.all()
    return render(request,'allstudent.html',{'datas':allstudent})



def Student_delete(request,id):
    data = Mystudent.objects.get(id=id)
    data.delete()
    return redirect('/student/studentviewall/')

 
# def Student_Update(request,id):
#     studentdata =  Mystudent.objects.get(id=id)
#     studentform = StudentMyform(instance=studentdata)

#     if request.method=='POST':
#         updated_data = StudentMyform(request.POST,instance=studentdata)
#         if updated_data.is_valid():
#             updated_data.save()
#         return redirect('StUpdate')
        
#     return render(request,'studentupdate.html',{'studentform':studentform,'data':studentdata})
    
def Student_Update(request,id):
    studentdata =  Mystudent.objects.get(id=id)
    studentform = StudentMyform(instance=studentdata)

    if request.method=='POST':
        print('Error')
        uname   = request.POST['name']
        udesign = request.POST['designation']
        upay    = request.POST['pay']

        studentdata.name = uname
        studentdata.designation = udesign
        studentdata.pay = upay
        studentdata.save()
        print('Data saved')
        return redirect('viewallpage')
        
    return render(request,'studentupdate.html',{'studentform':studentform,'data':studentdata})

def Student_Update(request, id):
    studentdata =  Mystudent.objects.get(id=id)
    studentform = StudentMyform(instance=studentdata)

    if request.method == 'POST':
        obj = Mystudent.objects.filter(id=id)
        obj.update(name=request.POST['name'], designation=request.POST['designation'],pay=request.POST['pay'])
        print('Updated by queryset')
        return redirect('viewallpage')

    return render(request,'studentupdate.html',{'studentform':studentform,'data':studentdata})
from django.shortcuts import render,redirect
from testapp.models import Employee
from .forms import EmployeeForm
# Create your views here.
def retrive_view(request):
    emp_list=Employee.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})

def insert_view(request):
    form = EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/') 
    return render(request,'testapp/insert.html',{'form':form})

def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')

def update_view(request,id):
    employee=Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)  # to get ser provided data into the form directly
    if request.method=='POST':
        form = EmployeeForm(request.POST,instance=employee)  # to update the data in the same id we get otherwise new record will be added
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/update.html',{'form':form})

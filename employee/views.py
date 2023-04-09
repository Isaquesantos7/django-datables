from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from employee.models import Employee
from employee.forms import EmployeeForm
from django.contrib import messages

def employee_relatorio(request):
    employees = Employee.objects.all()
    
    return render(request, './tabelas/TabelaEmployee.html', context={'employees':employees})

def employee(request):
    
    if request.method == 'GET':

        form = EmployeeForm()

        context = {
            'form':form
        }

        return render(request ,'./forms/formulario.html', context=context)
    
    else: 
        form = EmployeeForm(request.POST)

        if form.is_valid():
            employee = form.save()
            form = EmployeeForm()
            messages.success(request, 'Employee inserted with success!')
        
        context = {
            'form':form
        }

        return render(request, './forms/formulario.html', context=context)

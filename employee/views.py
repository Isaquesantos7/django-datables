from django.shortcuts import redirect, render
from employee.models import Employee
from employee.forms import EmployeeForm
from django.contrib import messages

# HTTP
from django.http import HttpResponseRedirect, HttpResponse

# JSON
from django.http import JsonResponse

# IMPORT LOGIN
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# LIST ALL OF EMPLOYEES
@login_required(login_url='/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def employee_relatorio(request):
    employees = Employee.objects.all()
    
    return render(request, './tabelas/TabelaEmployee.html', context={'employees':employees})

# SAVING FORMS
@login_required(login_url='/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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

# RETURN ALL OF DATA AS JSON
@login_required(login_url='/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def employee_json(request):
    employees = Employee.objects.all()
    data = [employee.get_data() for employee in employees]
    response = {'data' : data}
    return JsonResponse(response)

# LOGIN
def login_auth(request,):
    if request.user == None or request.user == '' or request.user.username == '':
        return render(request, 'login.html')
    else:
        return HttpResponseRedirect('/')
    
# LOGIN-USER
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'User athenticated with success!')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Enter your data correctly.')
            return HttpResponseRedirect('/')
    else:
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
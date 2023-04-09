from django.urls import path
from employee.views import employee_relatorio, employee

urlpatterns = [
    path('', employee_relatorio, name='index'),
    path('addEmployee/', employee, name='addEmployee'),
]
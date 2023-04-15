from django.urls import path
from employee.views import employee_relatorio, employee, employee_json
from employee.views import login_auth, loginUser, logoutUser

urlpatterns = [
    path('', employee_relatorio, name='index'),
    path('addEmployee/', employee, name='addEmployee'),

    # JSON RESPONSE
    path('json/', employee_json, name='json'),

    # LOGIN
    path('login/', login_auth, name='login'),
    path('login_user', loginUser, name='login_user'),
    path('logout_user/', logoutUser, name='logout_user')
]
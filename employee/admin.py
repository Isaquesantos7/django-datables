from django.contrib import admin
from employee.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    fields = ['name','email','job','active']
    list_per_page=8 
    search_fields=['name']
    list_display = ['id','name','email','job','active']

admin.site.register(Employee, EmployeeAdmin)
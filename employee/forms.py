from django import forms
from employee.models import Employee

class EmployeeForm(forms.ModelForm):
    name = forms.CharField(
        max_length=60,
        required=True,
        widget=forms.TextInput(attrs={'required': 'true', 'class':'form-control'}) 
    )

    email = forms.CharField(
        max_length=254,
        required=True,
        widget= forms.EmailInput(attrs={'required': 'true', 'class':'form-control'})
        
    )
    
    job = forms.CharField(
        max_length=160,
        required=True,
        widget=forms.TextInput(attrs={'required': 'true', 'class':'form-control'})
    )

    active = forms.BooleanField()

    class Meta:
        model = Employee
        fields = ['name', 'email', 'job', 'active']
from django import forms
from .models import Employee, Companies, Contract


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name', 'email', 'phone', 'addres', 'profession')


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Companies
        fields = ('name', 'addres', 'phone')


class ContracForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = ('start_date', 'end_date', 'employee', 'company', 'salary')

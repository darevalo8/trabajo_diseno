from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .forms import EmployeeForm, CompanyForm, ContracForm
from .models import Employee, Companies, Contract


class IndexView(ListView):
    model = Employee
    template_name = 'proyecto/index.html'
    context_object_name = 'employee'


class AddEmployee(CreateView):
    form_class = EmployeeForm
    #template_name = 'proyecto/prueba.html'
    template_name = 'proyecto/index.html'
    success_url = '/'


class UpdateEmloyee(UpdateView):
    form_class = EmployeeForm
    model = Employee
    template_name = 'proyecto/prueba.html'
    success_url = '/'


class DeleteEmployee(DeleteView):
    model = Employee
    template_name = 'proyecto/delete.html'
    success_url = '/'


class ListCompany(ListView):
    model = Companies
    template_name = 'proyecto/compania.html'
    context_object_name = "compania"


class AddCompany(CreateView):
    model = Companies
    form_class = CompanyForm
    template_name = 'proyecto/prueba.html'
    success_url = '/list-company'


class UpdateCompany(UpdateView):
    model = Companies
    form_class = CompanyForm
    template_name = 'proyecto/prueba.html'
    success_url = '/list-company'


class DeleteCompany(DeleteView):
    model = Companies
    template_name = 'proyecto/delete.html'
    success_url = '/list-company'


class ListContract(ListView):
    model = Contract
    template_name = 'proyecto/contratos.html'
    context_object_name = 'contrato'


class AddContract(CreateView):
    model = Contract
    form_class = ContracForm
    template_name = 'proyecto/prueba.html'
    success_url = '/list-contratos'


class UpdateContract(UpdateView):
    model = Contract
    form_class = ContracForm
    template_name = 'proyecto/prueba.html'
    success_url = '/list-contratos'


class DeleteContract(DeleteView):
    model = Contract
    template_name = 'proyecto/delete.html'
    success_url = '/list-contratos'

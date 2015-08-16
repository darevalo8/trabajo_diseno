from django.conf.urls import url
from proyecto import views
from proyecto.views import IndexView, AddEmployee, UpdateEmloyee, DeleteEmployee, ListCompany
from proyecto.views import AddCompany, UpdateCompany, DeleteCompany, ListContract, AddContract
from proyecto.views import UpdateContract, DeleteContract
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^crear-employee$', AddEmployee.as_view(), name='add-employee'),
    url(r'^update-employee/(?P<pk>\d+)$', UpdateEmloyee.as_view(), name='prueba'),
    url(r'^delete-employee/(?P<pk>\d+)$', DeleteEmployee.as_view(), name='delete-employee'),
    url(r'^list-company$', ListCompany.as_view(), name='list-comania'),
    url(r'^crear-company$', AddCompany.as_view(), name='add-comania'),
    url(r'^update-company/(?P<pk>\d+)$', UpdateCompany.as_view(), name='update-compania'),
    url(r'^delete-company/(?P<pk>\d+)$', DeleteCompany.as_view(), name='delete-compania'),
    url(r'^list-contratos$', ListContract.as_view(), name='list-contratos'),
    url(r'^crear-contrato$', AddContract.as_view(), name='add-contratos'),
    url(r'^update-contract/(?P<pk>\d+)$', UpdateContract.as_view(), name='update-contratos'),
    url(r'^delete-contract/(?P<pk>\d+)$', DeleteContract.as_view(), name='delete-contratos'),

]

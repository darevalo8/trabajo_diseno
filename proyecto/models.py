import datetime
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.IntegerField()
    addres = models.CharField(max_length=100)
    profession = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Companies(models.Model):
    name = models.CharField(max_length=80)
    addres = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

class Contract(models.Model):
    start_date = models.DateField(default=datetime.datetime.today)
    end_date = models.DateField()
    employee = models.ForeignKey(Employee)
    company = models.ForeignKey(Companies)
    salary = models.IntegerField()

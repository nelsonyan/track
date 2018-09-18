

from django.shortcuts import render
from . import models
from employee.forms import EmployeeInputForms
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView,)
# Create your views here.

class EmployeeOutput(ListView):
    model = models.EmployeeList
    context_object_name = 'employee_list'
    template_name = 'employee_list.html'
        #if missing, it is looking for EmployeeList_list.html
        #employee_list.pk used in empllyee_list.html

class EmployeeInput(CreateView):
    model = models.EmployeeList
    template_name = 'employee_input.html'
        #the context_object_name is form, cannot be changed?
    form_class = EmployeeInputForms

class EmployeeUpdate(UpdateView):
    model = models.EmployeeList
    form_class = EmployeeInputForms
    context_object_name = 'employee_detail'
    template_name = 'employee_detail.html'

# class EmployeeDelete(DeleteView):
    # model = models.EmployeeList
    # fields = '__all__'
    # template_name = 'employee_input.html'
        #the tag 'form' can still be used

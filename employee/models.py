

from django.db import models
from django.urls import reverse
# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length = 20, unique = True)

    def __str__(self):
        return self.department

class RemoteAccess(models.Model):
    remote_access = models.CharField(max_length = 20, blank = True)
    def __str__(self):
        return self.remote_access

class EmployeeList(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    department = models.ForeignKey(Department, on_delete = models.SET_NULL, null = True, blank = True)
    email = models.EmailField(blank = True)
    phone_ex = models.CharField(max_length = 10, blank = True)
    cell = models.CharField(max_length = 20, blank = True)
    remote_access = models.ForeignKey(RemoteAccess, on_delete = models.SET_NULL, null = True, blank = True)
    message = models.TextField(max_length = 2000, blank = True)

    def __str__(self):
        return self.first_name
            # id = models.AutoField(primary_key=True)  this is by defautl

    def get_absolute_url(self):
        return reverse('employee:employee_list')

    class Meta:
        ordering = ["phone_ex"]

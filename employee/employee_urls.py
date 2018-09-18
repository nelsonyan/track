

from django.urls import path
from . import views

app_name = 'employee'
urlpatterns = [
    path('output/', views.EmployeeOutput.as_view(), name = 'employee_list'),
    path('input/', views.EmployeeInput.as_view(), name = 'employee_input'),
    path('update/<int:pk>/', views.EmployeeUpdate.as_view(), name = 'employee_update'),
]

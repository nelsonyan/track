

from django import forms
from employee.models import EmployeeList

class EmployeeInputForms(forms.ModelForm):
    class Meta():
        model = EmployeeList
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'size':110}),
            'last_name': forms.TextInput(attrs={'size':110}),
            'email': forms.TextInput(attrs={'size':110}),
            'phone_ex': forms.TextInput(attrs={'size':110}),
            'cell': forms.TextInput(attrs={'size':110}),
            'message': forms.Textarea(attrs={'rows':8, 'cols':110}),
        }

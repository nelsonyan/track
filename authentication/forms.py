

from django import forms
from django.contrib.auth.models import User
from authentication.models import MarklynUser

class MarklynUserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
        #not sure if this is necessary
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
    # class Meta():
    #     model = MarklynUser
    #     fields = '__all__'
    # if this way, only shows a dropdown of user that is pre-build with admin panel and user user_pic
    # there is no open field to enter anything, the build in LN FN and etc are not shown
# class MarklynPicForm(forms.ModelForm):
#     class Meta():
#         model = MarklynUser
#         fields = ('user_pic',)

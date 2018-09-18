from django.shortcuts import render
from authentication.forms import MarklynUserForm
    # marklynPicForm
# from home.views import HomePage
# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def register(request):
    registered = False
    if request.method =='POST':
        marklyn_user_form_tag = MarklynUserForm(data = request.POST)


        if marklyn_user_form_tag.is_valid():
            registered_user = marklyn_user_form_tag.save()
            registered_user.set_password(registered_user.password)
            registered_user.save()


            registered = True
        else:
            print(marklyn_user_form_tag.errors)
    else:
        marklyn_user_form_tag = MarklynUserForm()


    return render(request, 'registration.html',
        {'registered': registered,
        'marklyn_user_form_tag': marklyn_user_form_tag,})

def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home:home_page'))
            else:
                return HttpResponse("Account not active")
        else:
            print('site is being hacked')
            print('username: {} and password {}'.format(username, password))

            return render(request, 'invalid.html')
    else:
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)
        
    return HttpResponseRedirect(reverse('home:home_page'))

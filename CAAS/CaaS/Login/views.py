from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Connector.models import SSCConnector
from Jira.models import Jira




@login_required(login_url='/login/')
def ssc_view(request):
    return render(request, 'dashboard/ssc.html')

@login_required(login_url='/login/')
def home_view(request):
    return render(request, 'dashboard/home.html')

def user_login(request):
    if request.POST:
        singin_data = request.POST.dict()
        username = singin_data.get('email')
        password = singin_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            ssc_id = request.user
            ssc_data = SSCConnector.objects.filter(user_id=request.user).first()
            jira_data = Jira.objects.filter(user_id=request.user).first()
            # return redirect('/home/', ssc_data=ssc_data)
            return render(request, 'dashboard/home.html', {'ssc_data': ssc_data, 'jira_data': jira_data})
        else:
            messages.error(request, f'Invalid Username and Password')
            return redirect('/login/')
            # raise ValidationError("Invalid Username and Password!!")
    else:
        return render(request, 'login/login.html')

  


def user_register(request):
    if request.POST:
        singup_data = request.POST.dict()
        first_name = singup_data.get('first_name')
        last_name = singup_data.get('last_name')
        email = singup_data.get('email')
        username = singup_data.get('email')
        password = singup_data.get('password')
        cpassword = singup_data.get('cpassword')
        if password != cpassword:
            messages.error(request, f'Password and Confirm_password does not match"!!')
            return redirect('/register/') 

        user = User.objects.filter(username=username)
        if user.count():
            messages.warning(request, f'Account with given email id is already registered!!! ')
            return redirect('/register/')

        else:
            new_user = User.objects.create_user(username, first_name=first_name, last_name=last_name, password=password, email=email)
            new_user.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('/login/')
    return render(request, 'login/register.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/login/')
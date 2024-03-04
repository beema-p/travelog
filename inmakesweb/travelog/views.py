from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid user login")
            return redirect('login')

    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        username = request.POST['user']
        firstname = request.POST['f_name']
        lastname = request.POST['l_name']
        mail = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_pass']

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "this username already exist")
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request, "this mail already taken by someone")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                email=mail, password=password)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'Passwords are incorrect')
            return redirect('register')

    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
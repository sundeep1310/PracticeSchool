from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout


# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                auth_login(request, user)
                
                return redirect('/projects')

    return render(request, 'account/login.html')


def signup(request):
    if request.method=='POST':
       name=request.POST.get('name','')
       email=request.POST.get('email','')
       password1=request.POST.get('password1','')
       password2=request.POST.get('password2','')
       if name and email and password1 and password2:
           user=User.objects.create_user(name,email,password1)
           print("User Created:",user)
           
           return redirect('/login/')
       else:
           print("something went wrong")
    else:
        print("just show the form")
    return render(request,'account/signup.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')



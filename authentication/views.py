from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .authenticator import auth
from .forms import formsignup, vogueuser, DivErrorList
from .models import VogueUser
from main.models import Cart
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import asyncio


def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == 'POST':
        form = formsignup(request.POST, error_class=DivErrorList)
        
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            login(request, new_user)

            mailer(form.cleaned_data['email'],form.cleaned_data['username'])

            bg = User.objects.get(username=form.cleaned_data['username'])
            vg = VogueUser.objects.create(
                user=bg,
                name=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )
            vg.save()
            #Create cart instance for each user
            cart = Cart.objects.create(user=bg)
            cart.save()
            print("Success")
            return redirect('/store')
        else:
            print(form.errors)
            return render(request, "signup.html", {'errors': form.errors})
    return render(request, "signup.html")
def signin(request):
    if request.method == 'POST':
        usermail=request.POST.get('email')
        userpassword=request.POST.get('password')
        print(usermail,userpassword)
        authuser = auth.authenticate(request,username=usermail,password=userpassword)
        if authuser is not None:
            login(request,authuser)
            return redirect('/store')
        else:
            print(auth)
            return render(request, "signin.html", {'errors': "email of password is incorrect"})        
    return render(request, "signin.html")

def logoutuser(request):
    logout(request)
    return redirect('/')

def mailer(mail, name):
    send_mail(
    "Vogue Walk - Thanks for Signing Up",
    "Hey "+name+'''Greetings!\n Thank For Signing up,we are delighted to have you. 
    We offer wide range fashion styles with uncompromised quality at affordable luxury, 
    and we hope to see your shop with us more!!!\n
    Thank You!\n
    With Regards\n
    Team Vogue Walk
    ''',
    settings.EMAIL_HOST_USER,
    [mail],
    fail_silently=False)
    return True
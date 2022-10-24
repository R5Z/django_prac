from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as loginsession

# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        if password == password:
            Usermodel.objects.create_user(username = username, password = password, phone = phone, address = address)
            return redirect('/login')

def login(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/home')
        else:
            return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        me = User.objects.get(username=username)
        if me.password == password:
            auth.login(request, me)
            request.session['user'] = me.username
            return redirect('/home')
        else:
            return render(request, 'login.html')

def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    else:
        return redirect('/login')

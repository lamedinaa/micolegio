# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout

def index(request):
    return render(request,'front/index.html')

def loginview(request):
    msjAuth = ''
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user is not None and user.is_active:
            login(request,user)
            print "verificacion "
            print user.perfil.perfil
            if user.perfil.perfil == 0:
                return HttpResponseRedirect('/director/home/')
            elif user.perfil.perfil == 1:
                return HttpResponseRedirect('/director/home')
            else:
                msjAuth = "Usuario sin asignar perfil"
        else:
            msjAuth = "Usuario o contraseña incorrecta"
    return render(request,'front/login.html',{"msjAuth":msjAuth})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/')

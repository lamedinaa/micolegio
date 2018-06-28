# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required

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
            if user.perfil.perfil == 0: ## perfil administrador
                return HttpResponseRedirect('/admin/inicio/')
            elif user.perfil.perfil == 1: ## perfil director
                return HttpResponseRedirect('/director/inicio/')
            elif user.perfil.perfil == 2:
                return HttpResponseRedirect('/profesores/inicio/')
            elif user.perfil.perfil == 3:
                return HttpResponseRedirect('/padres/inicio/')
            else:
                msjAuth = "Usuario sin asignar perfil"
        else:
            msjAuth = "Usuario o contraseña incorrecta"
    return render(request,'front/login.html',{"msjAuth":msjAuth})

@login_required
def inicioAdmin(request):
    return render(request,'admin/inicio.html',{
    "active":{1:"home",2:"inicio"}
    })

def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/')

# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apps.director.forms import *
from apps.director.models import *
from django.db import transaction,IntegrityError
from django.db.models import Q
from mensajeria.correosfront import mail_codigoQR
from django.core.mail import EmailMessage
from micolegio.settings import EMAIL,KEY

@login_required
def asociarPagos(request):
    return render(request,'director/asociarpagos.html',{
    "active":{1:"tesoreria",2:"asociarPagos"}
    })

@login_required
def listaPagos(request):
    return render(request,'director/listapagos.html',{
    "active":{1:"tesoreria",2:"listaPagos"}
    })


@login_required
def inicio(request):
    return render(request,'director/inicio.html',{
    "active":{1:"home",2:"inicio"}
    })

@login_required
def editarAlumno(request,id_alumno):
    alumno = Alumnos.objects.get(id = id_alumno)
    return render(request,'director/editarAlumnos.html',{
    "alumno":alumno,
    "active":{1:"tablero",2:"miEquipo"}
    })


def QRpublico(request,key,documento_alumno,id_alumno):
    alumno = Alumnos.objects.get(id = id_alumno)
    print key
    print alumno.keyQR
    if key == alumno.keyQR:
        return render(request,'director/codigoQR.html',{
        "idAlumno":id_alumno,
        "documentoAlumno":documento_alumno,
        })
    return render(request,'front/error500.html',{})

@login_required
def generarQR(request,id_alumno,documento_alumno,envio):
    if envio == "0":
        return render(request,'director/codigoQR.html',{
        "idAlumno":id_alumno,
        "documentoAlumno":documento_alumno,
        })
    elif envio == "1":
        emailfallidos = []
        try:
            key = KEY(64)
            alumno = Alumnos.objects.select_related().get(id = id_alumno)
            alumno.keyQR = key
            padres = alumno.padres.all()
            nombreEscuela = request.user.perfil.escuela.all()[0].nombre
            asunto = "{0} código QR ".format(nombreEscuela)
            alumno.save()
            for padre in padres:
                bodyEmail = mail_codigoQR(padre.first_name,alumno.nombres,id_alumno,documento_alumno,key)
                email = EmailMessage(asunto,bodyEmail,EMAIL,[padre.email])
                email.content_subtype = "html"
                result = email.send()
                if result == 0 :
                    emailfallidos.append(padre.email)
            if len(emailfallidos)>0:
                datos = {"status":"error",
                "msj":"error en un correo",
                "fallos":emailfallidos
                }
            else:
                datos = {"msj":"Email exitoso"}
            return JsonResponse(datos)
        except:
            datos = {"status":"error",
            "msj":"email fallido"
            }
            return JsonResponse(datos)


@login_required
def miEquipo(request):
    escuela = request.user.perfil.escuela.all()[0]
    alumnos = Alumnos.objects.filter(escuela = escuela)
    return render(request,'director/miEquipo.html',{
    "active":{1:"tablero",2:"miEquipo"},
    "alumnos":alumnos,
    } )

def misSelecciones(request):
    escuela = request.user.perfil.escuela.all()[0]
    selecciones = Seleccion.objects.filter(escuela = escuela)
    return render(request,'director/misSelecciones.html',{
    "selecciones":selecciones,
    'active':{1:"tablero",2:"misSelecciones"}})

def misEntrenadores(request):
    escuela = request.user.perfil.escuela.all()[0]
    entrenadores = User.objects.select_related().filter(perfil__perfil = 2,perfil__escuela = escuela)
    return render(request,'director/misEntrenadores.html',{
    'entrenadores': entrenadores,
    'active':{1:'tablero',2:'misEntrenadores'}})

def listaPadres(request):
    escuela = request.user.perfil.escuela.all()[0]
    padres = User.objects.select_related().filter(perfil__perfil = 4,perfil__escuela = escuela)
    return render(request,'director/listapadres.html',{
    'padres': padres,
    'active':{1:'tablero',2:'listapadres'}})

@login_required
def insertProfesores(request):
    """esta funcion solo es para renderizar, el insert de staff,padres,profes se insertan
    la funcion  insertFormUsers pues todos son Users"""
    return render(request,'director/insertprofesores.html',{"active":{1:"registro",2:"profesores"}} )


@login_required
def insertPadres(request):
    """esta funcion solo es para renderizar, el insert de staff,padres,profes se insertan
    la funcion  insertFormUsers pues todos son Users"""
    return render(request,'director/insertpadres.html',{"active":{1:"registro",2:"padres"}} )

@login_required
def insertEstudiantes(request):
    colegio = request.user.perfil.escuela.all()[0]
    padres = Perfil.objects.prefetch_related().filter(escuela = colegio, perfil = 4 )
    return render(request,'director/insertestudiantes.html',{
    "active":{1:"registro",2:"estudiantes"},
    "padres":padres,
    } )

def insertSeleccion(request):
    escuela  = request.user.perfil.escuela.all()[0]
    query = Q()
    query = Q(perfil__perfil = 1)|Q(perfil__perfil = 2)
    entrenadores = User.objects.filter(perfil__escuela = escuela).filter(query)
    print entrenadores
    return render(request,'director/insertseleccion.html',{
    "entrenadores": entrenadores,
    "active":{1:"registro",2:"seleccion"}
    })

@login_required
def insertStaff(request):
    """esta funcion solo es para renderizar, el insert de staff,padres,profes se insertan
    la funcion  insertFormUsers pues todos son Users"""
    return render(request,'director/insertstaff.html',{"active":{1:"registro",2:"staff"}} )

@login_required
def validarUser(request):
    print "validacion de usuario"
    email = request.GET.get('email',None)
    datos = {
        'validacion': User.objects.filter(username__iexact = email).exists()
    }
    print datos
    return JsonResponse(datos)


@login_required
def insertSeleccionForm(request):
    if request.POST:
        nombreSeleccion = request.POST['nombreseleccion']
        entrenadorId = request.POST["entrenadorId"]
        try:
            with transaction.atomic():
                print "entrenador"
                entrenador = User.objects.get(id = int(entrenadorId))
                print entrenador
                seleccion = Seleccion(nombre = nombreSeleccion,profesor = entrenador)
                seleccion.save()
        except:
            print "error en guardar"
            passs
    datos = {"msj":"registro exitoso"}
    return JsonResponse(datos)

@login_required
def insertFormUsers(request):
    if request.FILES:
        u = request.FILES['imgUser'].name.split(".")[1]
        extension = u.encode('ascii','ignore')
        lastUserId = str(User.objects.latest("id").id+1)
        nombreImg = lastUserId +"."+ extension
        request.FILES['imgUser'].name = nombreImg
    user_form = UserForm(request.POST)
    perfil_form = PerfilUserForm(request.POST,request.FILES)
    print perfil_form.errors
    if  user_form.is_valid() and perfil_form.is_valid():
        escuela = request.user.perfil.escuela.all()[0]
        usuario_perfil = perfil_form.save(commit=False)
        usuario = user_form.save()
        usuario_perfil.user = usuario
        usuario_perfil.save()
        usuario_perfil.escuela.add(escuela)
        usuario_perfil.save()
        datos = {"msj":"registo exitoso"}
        return JsonResponse(datos)
    else:
        print "formularios no validos"

@login_required
def insertFormEstudiantes(request):
    if request.FILES:
        u = request.FILES['imgEstudiante'].name.split(".")[1]
        extension = u.encode('ascii','ignore')
        lastAlumnoId = str(Alumnos.objects.latest("id").id + 1)
        request.FILES["imgEstudiante"].name= lastAlumnoId +"."+ extension
    alumnos_form = AlumnosForm(request.POST,request.FILES)
    if alumnos_form.is_valid():
        try:
            with transaction.atomic():
                escuela = request.user.perfil.escuela.all()[0]
                listaPadres = request.POST.getlist("padresId")
                query = Q()
                for padre in listaPadres:
                    query  = query|Q(id = int(padre))
                padresObj = User.objects.filter(query)
                alumno = alumnos_form.save()
                alumno.escuela.add(escuela)
                for padre in padresObj:
                    alumno.padres.add(padre)
                alumno.save()
        except:
            pass
    data = {"msj":"registro exitoso"}
    return JsonResponse(data)


@login_required
def editarEstudianteForm(request):
        #
        # alumno = Alumnos.objects.prefetch_related('padres').get(id = request.POST['id_alumno'])
        # alumno.nombres = request.POST["nombres"]
        # alumno.apellidos = request.POST["apellidos"]
        # alumno.numDocumento = request.POST["numDocumento"]
        # alumno.email = request.POST["email"]
        # ### ME FALTA EDITAR FECHA DE NACIMIENTO!!!!!
        #
        # ##editando padres del estudiante
        # idListaPadres = request.POST.getlist('padresId')
        # query = Q()
        # for idPadre in idListaPadres:
        #     query = query|Q(id = int(idPadre))
        # padresObj = User.objects.filter(query)
        # alumno.padres.all().delete()
        # for padre in padresObj:
        #     alumno.padres.add(padre.id)
        # ####editando la imagen si existe
        # if request.FILES:
        #     u = request.FILES['imgEstudiante'].name.split(".")[1]
        #     extension = u.encode('ascii','ignore')
        #     lastAlumnoId = str(Alumnos.objects.latest("id").id + 1)
        #     request.FILES["imgEstudiante"].name= lastAlumnoId +"."+ extension
        #     path_inicial = alumno.imgAlumno.path
        #     path_nuevo  = 'imgAlumno/' + request.FILES["imgEstudiante"].name
        #     os.rename(path_inicial,path_nuevo)
        # alumno.save()
        # # try:
        # #     with transaction.atomic():
        # #         print "procesando formulario"
        # #         alumno = Alumnos.objects.prefetch_related('padres').get(id = request.POST['id_alumno'])
        # #         idListaPadres = request.POST.getlist('padresId')
        # #         for idPadre in idListaPadres:
        # #             query = query|Q(id = int(idPadre))
        # #         padresObj = User.objects.filter(query)
        # #
        # #
        # # except:
        # #     print "no registra"
        # #     pass
        data = {"msj":"registro exitoso"}
        return JsonResponse(data)

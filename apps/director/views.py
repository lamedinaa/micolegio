from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apps.director.forms import *
from django.db import transaction,IntegrityError
from django.db.models import Q

@login_required
def generarQR(request,id_alumno,documento_alumno):
    return render(request,'director/codigoQR.html',{
    "idAlumno":id_alumno,
    "documentoAlumno":documento_alumno,
    })

@login_required
def miEquipo(request):
    escuela = request.user.perfil.escuela.all()[0]
    alumnos = Alumnos.objects.filter(escuela = escuela)
    return render(request,'director/miEquipo.html',{
    "active":{1:"tablero",2:"miEquipo"},
    "alumnos":alumnos,
    } )

def misSelecciones(request):
    return render(request,'director/misSelecciones.html',{'active':{1:"tablero",2:"misSelecciones"}})

def misEntrenadores(request):
    return render(request,'director/misEntrenadores.html',{'active':{1:'tablero',2:'misEntrenadores'}})

@login_required
def insertProfesores(request):
    return render(request,'director/insertprofesores.html',{"active":{1:"registro",2:"profesores"}} )


@login_required
def insertPadres(request):
    return render(request,'director/insertpadres.html',{"active":{1:"registro",2:"padres"}} )

@login_required
def insertEstudiantes(request):
    colegio = request.user.perfil.escuela.all()[0]
    padres = Perfil.objects.prefetch_related().filter(escuela = colegio)
    return render(request,'director/insertestudiantes.html',{
    "active":{1:"registro",2:"estudiantes"},
    "padres":padres,
    } )

@login_required
def insertStaff(request):
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

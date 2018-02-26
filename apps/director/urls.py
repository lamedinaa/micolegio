from django.conf.urls import include, url
from apps.director.views import *


urlpatterns = [
    url(r'^miequipo/$',miEquipo,name = "listaestudiantesUrls"),
    url(r'^misentrenadores/$',misEntrenadores,name = "misEntrenadoresUrls"),
    url(r'^misselecciones/$',misSelecciones,name = "misSeleccionesUrls"),
    url(r'^insertprofesores/$',insertProfesores, name = "insertprofesores"),
    url(r'^insertpadres/$',insertPadres,name = "insertpadresUrl"),
    url(r'^insertestudiantes/$',insertEstudiantes,name = "insertestudiantesUrl"),
    url(r'^insertstaff/$',insertStaff,name = "insertstaffUrl"),
    # peticiones AJAX
    url(r'^insertusersform/$',insertFormUsers,name = "insertFormUsersUrls"),
    url(r'^insertestudianteform/$',insertFormEstudiantes,name = "insertformestudianteUrl"),
    url(r'^validaruser/$',validarUser,name = "validaruserUrl"),
]

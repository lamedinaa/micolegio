from django.conf.urls import include, url
from apps.director.views import *


urlpatterns = [
    url(r'^home/$',homeDirector,name = "homedirectorUrls"),
    url(r'^insertprofesores/$',insertProfesores, name = "insertprofesores"),
    url(r'^insertpadres/$',insertPadres,name = "insertpadresUrl"),
    url(r'^insertestudiantes/$',insertEstudiantes,name = "insertestudiantesUrl"),
    url(r'^insertstaff/$',insertStaff,name = "insertstaffUrl"),
    # peticiones AJAX
    url(r'^insertusersform/$',insertFormUsers,name = "insertFormUsersUrls"),
    url(r'^insertestudianteform/$',insertFormEstudiantes,name = "insertformestudianteUrl"),
    url(r'^validaruser/$',validarUser,name = "validaruserUrl"),
]

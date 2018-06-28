from django.conf.urls import include, url
from apps.director.views import *

urlpatterns = [
    url(r'^inicio/$',inicio,name = "inicioUrls"),
    url(r'^miequipo/$',miEquipo,name = "listaestudiantesUrls"),
    url(r'^misentrenadores/$',misEntrenadores,name = "misEntrenadoresUrls"),
    url(r'^misselecciones/$',misSelecciones,name = "misSeleccionesUrls"),
    url(r'^listapadres/$',listaPadres,name = "listaPadresUrls"),
    url(r'^insertprofesores/$',insertProfesores, name = "insertprofesores"),
    url(r'^insertpadres/$',insertPadres,name = "insertpadresUrl"),
    url(r'^insertestudiantes/$',insertEstudiantes,name = "insertestudiantesUrl"),
    url(r'^insertstaff/$',insertStaff,name = "insertstaffUrl"),
    url(r'^insertseleccion/$',insertSeleccion,name="insertSeleccionUrl"),
    url(r'^generarqr/(?P<envio>\d+)/(?P<documento_alumno>\d+)/(?P<id_alumno>\d+)/$',generarQR,name="generarQrUrls"),
    url(r'^qrpublico/(?P<key>[0-9a-z]{1,128})/(?P<documento_alumno>\d+)/(?P<id_alumno>\d+)/$',QRpublico,name="QrpublicoUrls"),
    url(r'^listapagos/$',listaPagos,name="listaPagosUrl"),
    url(r'^asociarpagos/$',asociarPagos,name="asociarPagos"),
    # peticiones AJAX
    url(r'^insertseleccionform/$',insertSeleccionForm, name = "insertSeleccionesFormUrl"),
    url(r'^insertusersform/$',insertFormUsers,name = "insertFormUsersUrls"),
    url(r'^insertestudianteform/$',insertFormEstudiantes,name = "insertformestudianteUrl"),
    url(r'^validaruser/$',validarUser,name = "validaruserUrl"),
    url(r'^editaralumno/(?P<id_alumno>\d+)',editarAlumno, name = "editarAlumnoUrl"),
    url(r'^editarestudianteform/',editarEstudianteForm, name="editarEstudianteFormUrl"),
]

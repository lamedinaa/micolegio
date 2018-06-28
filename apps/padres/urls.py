from django.conf.urls import url
from apps.padres.views import *

urlpatterns = [
  url(r'^inicio/$',inicioPadres,name = "inicioPadresUrl"),
]

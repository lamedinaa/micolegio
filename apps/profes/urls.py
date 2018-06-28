from django.conf.urls import url
from apps.profes.views import *

urlpatterns = [
  url(r'^inicio/$',inicioProfes,name = "inicioPadresUrl"),
]

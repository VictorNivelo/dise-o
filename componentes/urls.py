from componentes.vistas import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("botones/", botones, name="botones"),
    path("entradas/", entradas, name="entradas"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('inicio/index', views.index),
    path('inicio/consultar-precios', views.consultar_precios),
    path('inicio/consultar-precios-js', views.consultar_precios_js),
    path('inicio/consultar-datos', views.consultar_datos),
    path('inicio/consultar-formulario', views.consultar_datos1),
]
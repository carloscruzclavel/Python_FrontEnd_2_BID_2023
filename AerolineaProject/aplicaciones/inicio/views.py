from django.shortcuts import render
import requests 

# Create your views here.

def index(request):
    return render(request, 'inicio/index.html')

def consultar_precios(request):
    pagina = 1
    if request.GET:
        pagina = int(request.GET['page'])

    url_binance='https://api.binance.com/api/v3/ticker/price'
    datos = requests.get(url_binance)

    contexto = {'precios': datos.json()[pagina*10-10:pagina*10:]}

    return render(request, 'inicio/consultar-precios.html', contexto)

def consultar_precios_js(request):
    return render(request, 'inicio/consultar-precios-js.html')


def consultar_datos(request):
    url_datos='https://jsonplaceholder.typicode.com/users'
    datos1 = requests.get(url_datos)

    contexto1 = {'datos': datos1.json()}

    return render(request, 'inicio/consultar-datos.html', contexto1)

def consultar_datos1(request):
    url_datos='https://jsonplaceholder.typicode.com/posts/1'
    datos2 = requests.get(url_datos)

    contexto2 = {'formulario': datos2.json()}

    return render(request, 'inicio/consultar-formulario.html', contexto2)

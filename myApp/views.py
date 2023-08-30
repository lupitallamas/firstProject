from django.shortcuts import render
#Importar HHTTP response
from  django.http import HttpResponse
# Create your views here.

#El cliente -> pide ->requests
#El Servidor -> Responde
def bienvenida(request):
    #Responder
    return  HttpResponse("Bienvenido")
    
def despedida(request):
    #Responder
    return  HttpResponse("Adios")

def saludo(request):
    #saludo a koder
    return HttpResponse("Hola koders")

def saludo_con_nombre(request,name):
    print("lo que yo imprimo es en mi terminar-->",name)
    return HttpResponse(f"Hola {name}")

def kodemia_mentor(request,tipo):
    if tipo == "mentor":
        print("Hello mentor here are your casses")
        mensaje="Hello mentor here are your casses"
    elif tipo == "koder":
        print("Hello Koder welcome to kodemia")
        mensaje="Hello Koder welcome to kodemia"
    else:
        print("You are not welcome here")
        mensaje = "You are not welcome here"
    return HttpResponse(mensaje)     
from django.shortcuts import render
#Importar HHTTP response
from  django.http import HttpResponse
# Create your views here.

def get_koder(request,koder_id):
    koders = [
        {"koder_id": 1,
         "name": "Miren",
         "last_name":"Llamas"},
        {"koder_id": 2,
         "name": "Fernando",
         "last_name":"Fernandez"},
        {"koder_id": 3,
         "name": "Rodrigo",
         "last_name":"Rodriguez"},
        ]
    koder_buscado = [koder for koder in koders if koder["koder_id"]==koder_id]
    return HttpResponse(f"tu koders:{koder_buscado}")


def list_koders(request):
    koders = [
         {"name": "Miren",
         "last_name":"Llamas"},
        {"name": "Fernando",
         "last_name":"Fernandez"},
        {"name": "Rodrigo",
         "last_name":"Rodriguez"}
        ]
    return HttpResponse(koders)    

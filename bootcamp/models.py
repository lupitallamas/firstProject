from django.db import models

# Create your models here.
#id--> autoincrement
#first_name --> string
#last_name  --> string
#generation --> string
#email --> string
#phone --> status -->(activo, dado de bajja)
#address --> string
#size --> (s, m, l)
#created_at --> date
#updated_at --> date


#las clases(modelos) van capitalizadas --> koder
#Los modelos heredan del modelo predetermiando de Django
#Cada modelo representa una tabla de sql
#Cada propiead de la clase(modelo) representa un atgributo en la tabla

class Koder(models.Model):
    """koder Model."""
    STATUSES = [
        ("active","Active"),
        ("inactive", "Inactive"),
        ("finished", "Finished"),
    ]
    SIZES =[
        ("s", "Small"),
        ("m", "Medium"),
        ("l", "Large"),
    ]
    first_name = models.CharField(max_length=255)  #-->string
    last_name = models.CharField(max_length=255)
    generation = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    status = models.CharField(max_length=8,choices=STATUSES, default="active")
    size = models.CharField(max_length=1, choices=SIZES, default="m")
    birthdate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True) # -->en cuanto se cree nos agrega la hora por automatico.
    updated_at = models.DateField(blank=True, null=True)
    
    
    
    #Representar como nos regresan al Koder.
    
    def __str__(self):
        return f"firstName -> {self.first_name}, lastName -> {self.last_name}"
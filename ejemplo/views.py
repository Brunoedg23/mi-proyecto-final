from django.shortcuts import render
from django.shortcuts import render
from ejemplo.models import Familiar

# Create your views here.
def index(request):
    return render(request, "ejemplo/saludar.html", 
    {"nombre":"German",
    "apellido":"Martinez"})

def index_dos(request, nombre, apellido):
    return render(request, "ejemplo/saludar.html", 
    {"nombre":nombre,
    "apellido":apellido})

def index_tres(request):
    return render(request, "ejemplo/saludar.html",
    {"notas": [1,2,3,4,5,6,7]}
    )

def imc(request, peso, altura):
    imc = int(gitpeso) * float(altura)
    return render(request, "ejemplo/imc.html", {"imc":imc})

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

def mostrar_un_solo_familiar(request, id):
    identificador = int(id)
    return render(request, "ejemplo/un_familiar.html", Familiar.objects.get(id=identificador))

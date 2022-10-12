from django.shortcuts import render

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
    imc = int(peso) * int(altura)
    return render(request, "ejemplo/imc.html", {"imc":imc})

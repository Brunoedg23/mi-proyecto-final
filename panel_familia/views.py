from django.shortcuts import render
from django.shortcuts import render
from ejemplo.models import Familiar
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

class FamiliarList(ListView):
  model = Familiar


class FamiliarCrear(CreateView):
  model = Familiar
  success_url = reverse_lazy("family")

  fields = ["nombre", "direccion", "numero_pasaporte", "fecha_nacimiento"]


class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"


class FamiliarActualizar(UpdateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte", "fecha_nacimiento"]

from django import forms
from ejemplo.models import (Familiar, FamiliarHobbie, FamiliarProfesion)

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte', 'fecha_nacimiento']

class ActualizarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class HobbieForm(forms.ModelForm):
  class Meta:
    model = FamiliarHobbie
    fields = ['nombre', 'hobbie']

class ProfesionForm(forms.ModelForm):
  class Meta:
    model = FamiliarProfesion
    fields = ['nombre', 'profesion']
"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ejemplo.views import (index, index_dos, index_tres, 
                           imc, monstrar_familiares, 
                           mostrar_un_solo_familiar, BuscarFamiliar, AltaFamiliar, Datos, Vivienda, 
                           BuscarVivienda)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar/<nombre>/<apellido>', index_dos),
    path('mostrar-notas/', index_tres),
    path('imc/<peso>/<altura>', imc),
    path('mi-familia/', monstrar_familiares),
    path('un_familiar/<id>', mostrar_un_solo_familiar),
    path('panel-familia/', include('panel_familia.urls')),
    path('mi-familia/buscar', BuscarFamiliar.as_view(),name="familiar-buscar"), 
    path('mi-familia/alta', AltaFamiliar.as_view(),name="familiar-alta"),
    path('blog/', include('blog.urls')),    
#    path('mi-familia/vivienda', Vivienda.as_view(),name="familiar-vivienda"),
#    path('mi-familia/datos', Datos.as_view(),name="familiar-datos"),
#    path('mi-familia/buscar_viviendas', BuscarVivienda.as_view(),name="familiar-buscar-vivienda"), 
  ]
 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
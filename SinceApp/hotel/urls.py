from django.urls import path
from django.contrib.auth.decorators import login_required 
from .views import  *


urlpatterns = [
    path('registrar_clientes/', login_required(registrar_clientes) , name = 'clientes'),
    path('datos/', login_required(baseD) , name = 'datos'),
    path('eliminar_cliente/<int:id>',login_required(eliminarC) , name= 'eliminar_cliente'),
    path('facturas/<int:id>', login_required(facturasC) , name = 'facturas'),
    path('excel/', login_required(generarExcel) , name = 'generarExcel'),
    path('editar/<int:id>', login_required(editarC), name = 'editarC'),
    path('ocultar/<int:id>', login_required(ocultarC), name = 'ocultar_cliente')
]
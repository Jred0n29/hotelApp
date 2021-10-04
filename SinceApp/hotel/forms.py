from django import forms
from django.db.models import fields
from .models import Clientes, Admin


class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [
                    'identificacion',
                    'nombres',
                    'apellidos',
                    'telefono',
                    'fecha_inicial',
                    'fecha_final',
                    'valor',
                    'comentario',
                ]
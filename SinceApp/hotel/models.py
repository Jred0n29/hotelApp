from django.db import models

# Create your models here.


class Clientes(models.Model):
    """Modelos correspondientes a los datos del cliente"""
    id = models.AutoField(primary_key=True)
    identificacion = models.BigIntegerField(blank=False, null=False)
    nombres = models.CharField(max_length=50, blank=False, null= False)
    apellidos = models.CharField(max_length=50, blank=False, null= False)
    telefono = models.BigIntegerField(blank= False, null= False)
    fecha_inicial = models.DateField(blank=False, null=False)
    fecha_final = models.DateField(blank= False, null=False)
    valor = models.BigIntegerField(blank=False, null=False)
    comentario = models.TextField()
    estado = models.BooleanField("estado", default=True)
    ocultar = models.BooleanField("ocultar", default=True)


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombres']

    def __str__(self):
        return f"""{self.nombres} {self.apellidos}"""



    
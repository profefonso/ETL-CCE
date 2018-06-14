from django.db import models

# Create your models here.

class Entidad(models.Model):
    Codigo = models.CharField(primary_key=True, max_length=25)
    Nombre = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.Nombre)

class EstadoProceso(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.Nombre)

class TipoProceso(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.Nombre)

class Proceso(models.Model):
    CodigoProceso = models.CharField(primary_key=True, max_length=20)
    ID_TipoProceso = models.ForeignKey(TipoProceso, null=True, blank=True, on_delete=models.CASCADE)
    ID_EstadoProceso = models.ForeignKey(EstadoProceso, null=True, blank=True, on_delete=models.CASCADE)
    Cuantia = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    CodigoEntidad = models.ForeignKey(Entidad, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.CodigoProceso)

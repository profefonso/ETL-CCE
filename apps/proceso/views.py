from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView

from apps.proceso.models import Proceso
from apps.proceso.forms import ProcesoForm

from apps.api_rest.models import Proceso_mdb, Entidad_mdb

from mongoengine.connection import _get_db


# Create your views here.


def index(request):
    return render(request, 'proceso/index.html')

def apietl(request):
    return render(request, 'proceso/apietl.html')

def norelacional(request):
    proceso = Proceso_mdb.objects.all()
    contexto = {'procesos': proceso}
    return render(request, 'proceso/norelacional.html', contexto)


def clean_mongodb(request):
    db = _get_db()
    db.drop_collection('proceso_mdb')
    return redirect('norelacional')


def etl_mongodb(request):
    try:
        # Extract: extraer.
        procesos_sql = Proceso.objects.all()
        for proceso_s in procesos_sql:
            # Transform: transformar.
            entidad_s = proceso_s.CodigoEntidad
            proceso_mc = Proceso_mdb(
                id=str(proceso_s.CodigoProceso),
                codigo=str(proceso_s.CodigoProceso),
                entidad=[{"codigo": str(entidad_s.Codigo), "nombre": str(entidad_s.Nombre)}],
                tipo=str(proceso_s.ID_TipoProceso),
                estado=str(proceso_s.ID_EstadoProceso),
                cuantia=str(proceso_s.Cuantia))
            # Load: cargar.
            try:
                proceso_mc.save()
            except Exception:
                print("error Save")
    except Exception:
        print("error ETL")
    return redirect('norelacional')


class Modelo_relacional(ListView):
    model = Proceso
    template_name = 'proceso/relacional.html'


class Create_proceso(CreateView):
    model = Proceso
    form_class = ProcesoForm
    template_name = 'proceso/proceso_form.html'
    success_url = reverse_lazy('relacional')

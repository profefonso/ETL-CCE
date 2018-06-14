from django.contrib import admin

from apps.proceso.models import Entidad
from apps.proceso.models import TipoProceso
from apps.proceso.models import EstadoProceso
from apps.proceso.models import Proceso

# Register your models here.

admin.site.register(Entidad)
admin.site.register(TipoProceso)
admin.site.register(EstadoProceso)
admin.site.register(Proceso)

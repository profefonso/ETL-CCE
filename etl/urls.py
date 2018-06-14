"""etl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include

from apps.proceso import views as pr
from apps.proceso.views import Modelo_relacional, Create_proceso


urlpatterns = [
    path('', pr.index, name='home'),
    path('relacional/', Modelo_relacional.as_view(), name='relacional'),
    path('relacional/new', Create_proceso.as_view(), name='nuevoproceso'),
    path('norelacional/', pr.norelacional, name='norelacional'),
    path('cleanmdb/', pr.clean_mongodb, name='cleanmdb'),
    path('etl_mongodb/', pr.etl_mongodb, name='etlmdb'),
    path('apietl/', pr.apietl, name='apietl'),
    url(r'^api/', include('apps.api_rest.urls')),
    url(r'^admin/', admin.site.urls),
    #path('admin/', admin.site.urls),
]

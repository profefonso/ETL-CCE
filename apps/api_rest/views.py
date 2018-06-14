from django.shortcuts import render

from rest_framework_mongoengine import viewsets as meviewsets
from apps.api_rest.serializers import ProcesoSerializer
from rest_framework import generics
from rest_framework import filters
from apps.api_rest.models import Proceso_mdb


class ProcesoViewSet(meviewsets.ModelViewSet):
    queryset = Proceso_mdb.objects.all()
    serializer_class = ProcesoSerializer


class ProcesoDetail(generics.ListCreateAPIView):
    serializer_class = ProcesoSerializer
    my_filter_fields = ('codigo', 'tipo')  # specify the fields on which you want to filter

    def get_kwargs_for_filtering(self):
        filtering_kwargs = {}
        for field in self.my_filter_fields:  # iterate over the filter fields
            field_value = self.request.query_params.get(field)  # get the value of a field from request query parameter
            if field_value:
                filtering_kwargs[field] = field_value
        return filtering_kwargs

    def get_queryset(self):
        queryset = Proceso_mdb.objects.all()
        filtering_kwargs = self.get_kwargs_for_filtering()  # get the fields with values for filtering
        if filtering_kwargs:
            queryset = Proceso_mdb.objects.filter(**filtering_kwargs)  # filter the queryset based on 'filtering_kwargs'
        return queryset


from django import forms

from apps.proceso.models import Proceso


class ProcesoForm(forms.ModelForm):

    class Meta:
        model = Proceso

        fields = [
            'CodigoProceso',
            'CodigoEntidad',
            'ID_TipoProceso',
            'ID_EstadoProceso',
            'Cuantia',
        ]
        labels = {
            'CodigoProceso': 'Codigo Proceso',
            'CodigoEntidad': 'Entidad',
            'ID_TipoProceso': 'Tipo',
            'ID_EstadoProceso': 'Estado',
            'Cuantia': 'Cuantia',
        }

        widgets = {
            'CodigoProceso': forms.TextInput(attrs={'class': 'form-control'}),
            'CodigoEntidad': forms.Select(attrs={'class': 'form-control'}),
            'ID_TipoProceso': forms.Select(attrs={'class': 'form-control'}),
            'ID_EstadoProceso': forms.Select(attrs={'class': 'form-control'}),
            'Cuantia': forms.TextInput(attrs={'class': 'form-control'}),
        }
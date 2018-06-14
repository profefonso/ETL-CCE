from rest_framework_mongoengine import serializers
from apps.api_rest.models import Proceso_mdb


class ProcesoSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Proceso_mdb
        fields = '__all__'
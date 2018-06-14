from django.db import models

from mongoengine import Document, EmbeddedDocument, fields

# Create your models here.

class Entidad_mdb(EmbeddedDocument):
    codigo = fields.StringField(required=True)
    nombre = fields.StringField(required=True)

    def __str__(self):
        return '{}'.format(self.nombre)

class Proceso_mdb(Document):
    id = fields.StringField(primary_key=True, required=True)
    codigo = fields.StringField(required=True)
    entidad = fields.ListField(fields.EmbeddedDocumentField(Entidad_mdb))
    tipo = fields.StringField(required=True, null=True)
    estado = fields.StringField(required=True, null=True)
    cuantia = fields.StringField(required=False, null=True)

    def __str__(self):
        return '{}'.format(self.codigo)
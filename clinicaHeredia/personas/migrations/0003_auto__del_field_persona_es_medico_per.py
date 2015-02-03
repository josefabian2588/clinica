# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Persona.es_medico_per'
        db.delete_column(u'personas_persona', 'es_medico_per')


    def backwards(self, orm):
        # Adding field 'Persona.es_medico_per'
        db.add_column(u'personas_persona', 'es_medico_per',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    models = {
        u'personas.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellidos_per': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cedula_per': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'correo_per': ('django.db.models.fields.EmailField', [], {'max_length': '70', 'blank': 'True'}),
            'foto_file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_per': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefonoAuxiliar_per': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'telefonoPrincipal_per': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['personas']
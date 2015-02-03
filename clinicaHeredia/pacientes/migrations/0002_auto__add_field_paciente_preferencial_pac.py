# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Paciente.preferencial_pac'
        db.add_column(u'pacientes_paciente', 'preferencial_pac',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Paciente.preferencial_pac'
        db.delete_column(u'pacientes_paciente', 'preferencial_pac')


    models = {
        u'pacientes.paciente': {
            'Enfermedad_pac': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'Meta': {'object_name': 'Paciente'},
            'comentario_pac': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numeroCarnet_pac': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['personas.Persona']"}),
            'preferencial_pac': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'personas.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellidos_per': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cedula_per': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'correo_per': ('django.db.models.fields.EmailField', [], {'max_length': '70', 'blank': 'True'}),
            'es_medico_per': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'foto_file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_per': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefonoAuxiliar_per': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'telefonoPrincipal_per': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['pacientes']
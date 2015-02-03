# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Medico'
        db.create_table(u'medicos_medico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigoMedico_med', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['personas.Persona'])),
        ))
        db.send_create_signal(u'medicos', ['Medico'])


    def backwards(self, orm):
        # Deleting model 'Medico'
        db.delete_table(u'medicos_medico')


    models = {
        u'medicos.medico': {
            'Meta': {'object_name': 'Medico'},
            'codigoMedico_med': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['personas.Persona']"})
        },
        u'personas.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellidos_per': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cedula_per': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'correo_per': ('django.db.models.fields.EmailField', [], {'max_length': '70', 'blank': 'True'}),
            'foto_file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_per': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefonoAuxiliar_per': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'telefonoPrincipal_per': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['medicos']
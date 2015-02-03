# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Persona'
        db.create_table(u'personas_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_per', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellidos_per', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cedula_per', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('telefonoPrincipal_per', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('telefonoAuxiliar_per', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('correo_per', self.gf('django.db.models.fields.EmailField')(max_length=70, blank=True)),
            ('foto_file', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('es_medico_per', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'personas', ['Persona'])


    def backwards(self, orm):
        # Deleting model 'Persona'
        db.delete_table(u'personas_persona')


    models = {
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

    complete_apps = ['personas']
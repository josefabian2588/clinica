# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Especialidad'
        db.create_table(u'especialidades_especialidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_esp', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'especialidades', ['Especialidad'])


    def backwards(self, orm):
        # Deleting model 'Especialidad'
        db.delete_table(u'especialidades_especialidad')


    models = {
        u'especialidades.especialidad': {
            'Meta': {'object_name': 'Especialidad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_esp': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['especialidades']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field especialidad on 'Medico'
        m2m_table_name = db.shorten_name(u'medicos_medico_especialidad')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('medico', models.ForeignKey(orm[u'medicos.medico'], null=False)),
            ('especialidad', models.ForeignKey(orm[u'especialidades.especialidad'], null=False))
        ))
        db.create_unique(m2m_table_name, ['medico_id', 'especialidad_id'])


    def backwards(self, orm):
        # Removing M2M table for field especialidad on 'Medico'
        db.delete_table(db.shorten_name(u'medicos_medico_especialidad'))


    models = {
        u'especialidades.especialidad': {
            'Meta': {'object_name': 'Especialidad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_esp': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'medicos.medico': {
            'Meta': {'object_name': 'Medico'},
            'codigoMedico_med': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'especialidad': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'is_especialidad_of'", 'symmetrical': 'False', 'to': u"orm['especialidades.Especialidad']"}),
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
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'SixpackParticipant', fields ['experiment_name', 'unique_attr']
        db.create_unique(u'djsixpack_sixpackparticipant', ['experiment_name', 'unique_attr'])


    def backwards(self, orm):
        # Removing unique constraint on 'SixpackParticipant', fields ['experiment_name', 'unique_attr']
        db.delete_unique(u'djsixpack_sixpackparticipant', ['experiment_name', 'unique_attr'])


    models = {
        u'djsixpack.sixpackparticipant': {
            'Meta': {'unique_together': "(('experiment_name', 'unique_attr'),)", 'object_name': 'SixpackParticipant'},
            'bucket': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'converted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'experiment_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unique_attr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['djsixpack']
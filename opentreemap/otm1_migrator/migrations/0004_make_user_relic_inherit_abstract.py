# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        make_int = self.gf('django.db.models.fields.IntegerField')

        db.rename_column(u'otm1_migrator_otm1userrelic', u'otm1_id', u'otm1_model_id')
        db.add_column(u'otm1_migrator_otm1userrelic', 'otm2_model_id',
                      make_int(default=-1), keep_default=False)

    def backwards(self, orm):
        db.delete_column(u'otm1_migrator_otm1userrelic', 'otm2_model_id')
        db.rename_column(u'otm1_migrator_otm1userrelic', u'otm1_model_id', u'otm1_id')

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'otm1_migrator.otm1commentrelic': {
            'Meta': {'unique_together': "((u'otm2_model_name', u'otm1_model_id', u'instance'),)", 'object_name': 'OTM1CommentRelic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['treemap.Instance']"}),
            'otm1_last_child_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'otm1_model_id': ('django.db.models.fields.IntegerField', [], {}),
            'otm2_model_id': ('django.db.models.fields.IntegerField', [], {}),
            'otm2_model_name': ('django.db.models.fields.CharField', [], {'default': "u'threadedcomment'", 'max_length': '255'})
        },
        u'otm1_migrator.otm1modelrelic': {
            'Meta': {'unique_together': "((u'otm2_model_name', u'otm1_model_id', u'instance'),)", 'object_name': 'OTM1ModelRelic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['treemap.Instance']"}),
            'otm1_model_id': ('django.db.models.fields.IntegerField', [], {}),
            'otm2_model_id': ('django.db.models.fields.IntegerField', [], {}),
            'otm2_model_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'otm1_migrator.otm1userrelic': {
            'Meta': {'object_name': 'OTM1UserRelic'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['treemap.Instance']"}),
            'otm1_model_id': ('django.db.models.fields.IntegerField', [], {}),
            'otm1_username': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'otm2_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['treemap.User']"})
        },
        u'treemap.benefitcurrencyconversion': {
            'Meta': {'object_name': 'BenefitCurrencyConversion'},
            'co2_lb_to_currency': ('django.db.models.fields.FloatField', [], {}),
            'currency_symbol': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'electricity_kwh_to_currency': ('django.db.models.fields.FloatField', [], {}),
            'h20_gal_to_currency': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'natural_gas_kbtu_to_currency': ('django.db.models.fields.FloatField', [], {}),
            'nox_lb_to_currency': ('django.db.models.fields.FloatField', [], {}),
            'o3_lb_to_currency': ('django.db.models.fields.FloatField', [], {}),
            'pm10_lb_to_currency': ('django.db.models.fields.FloatField', [], {}),
            'sox_lb_to_currency': ('django.db.models.fields.FloatField', [], {}),
            'voc_lb_to_currency': ('django.db.models.fields.FloatField', [], {})
        },
        u'treemap.boundary': {
            'Meta': {'object_name': 'Boundary'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857', 'db_column': "u'the_geom_webmercator'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'treemap.instance': {
            'Meta': {'object_name': 'Instance'},
            'adjuncts_timestamp': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'basemap_data': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'basemap_type': ('django.db.models.fields.CharField', [], {'default': "u'google'", 'max_length': '255'}),
            'boundaries': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['treemap.Boundary']", 'null': 'True', 'blank': 'True'}),
            'bounds': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857'}),
            'center_override': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'config': ('treemap.json_field.JSONField', [], {'blank': 'True'}),
            'default_role': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'default_role'", 'to': u"orm['treemap.Role']"}),
            'eco_benefits_conversion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['treemap.BenefitCurrencyConversion']", 'null': 'True', 'blank': 'True'}),
            'geo_rev': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'itree_region_default': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'url_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['treemap.User']", 'null': 'True', 'through': u"orm['treemap.InstanceUser']", 'blank': 'True'})
        },
        u'treemap.instanceuser': {
            'Meta': {'unique_together': "((u'instance', u'user'),)", 'object_name': 'InstanceUser'},
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['treemap.Instance']"}),
            'reputation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['treemap.Role']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['treemap.User']"})
        },
        u'treemap.role': {
            'Meta': {'object_name': 'Role'},
            'default_permission': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['treemap.Instance']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rep_thresh': ('django.db.models.fields.IntegerField', [], {})
        },
        u'treemap.user': {
            'Meta': {'object_name': 'User'},
            'allow_email_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '30', 'blank': 'True'}),
            'make_info_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'organization': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['otm1_migrator']

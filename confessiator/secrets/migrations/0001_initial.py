# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('secrets_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('secrets', ['UserProfile'])

        # Adding model 'WallObject'
        db.create_table('secrets_wallobject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='owned_walls', to=orm['secrets.UserProfile'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('secret_token', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('facebook_id', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('wall_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('moderated', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('admin_token', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal('secrets', ['WallObject'])

        # Adding M2M table for field admins on 'WallObject'
        db.create_table('secrets_wallobject_admins', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('wallobject', models.ForeignKey(orm['secrets.wallobject'], null=False)),
            ('userprofile', models.ForeignKey(orm['secrets.userprofile'], null=False))
        ))
        db.create_unique('secrets_wallobject_admins', ['wallobject_id', 'userprofile_id'])

        # Adding model 'Confession'
        db.create_table('secrets_confession', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('declined', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('posted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_change', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('wall', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['secrets.WallObject'])),
        ))
        db.send_create_signal('secrets', ['Confession'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('secrets_userprofile')

        # Deleting model 'WallObject'
        db.delete_table('secrets_wallobject')

        # Removing M2M table for field admins on 'WallObject'
        db.delete_table('secrets_wallobject_admins')

        # Deleting model 'Confession'
        db.delete_table('secrets_confession')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'secrets.confession': {
            'Meta': {'object_name': 'Confession'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'declined': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_change': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'posted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wall': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['secrets.WallObject']"})
        },
        'secrets.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'secrets.wallobject': {
            'Meta': {'object_name': 'WallObject'},
            'admin_token': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'admins': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['secrets.UserProfile']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderated': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_walls'", 'to': "orm['secrets.UserProfile']"}),
            'secret_token': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'wall_type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['secrets']
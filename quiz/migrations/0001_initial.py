# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Genre'
        db.create_table('quiz_genre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('quiz', ['Genre'])

        # Adding model 'Show'
        db.create_table('quiz_show', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('quiz', ['Show'])

        # Adding M2M table for field genre on 'Show'
        db.create_table('quiz_show_genre', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('show', models.ForeignKey(orm['quiz.show'], null=False)),
            ('genre', models.ForeignKey(orm['quiz.genre'], null=False))
        ))
        db.create_unique('quiz_show_genre', ['show_id', 'genre_id'])

        # Adding model 'Episode'
        db.create_table('quiz_episode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('show', self.gf('django.db.models.fields.related.ForeignKey')(related_name='episodes', to=orm['quiz.Show'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('episode_number', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('season', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('quiz', ['Episode'])

        # Adding model 'Question'
        db.create_table('quiz_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='questions', to=orm['auth.User'])),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('show', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Show'])),
            ('episode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Episode'], blank=True)),
        ))
        db.send_create_signal('quiz', ['Question'])

        # Adding model 'Choice'
        db.create_table('quiz_choice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('choice', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='choices', to=orm['quiz.Question'])),
        ))
        db.send_create_signal('quiz', ['Choice'])

        # Adding model 'Answer'
        db.create_table('quiz_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answer', unique=True, to=orm['quiz.Question'])),
            ('choice', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answer', unique=True, to=orm['quiz.Choice'])),
        ))
        db.send_create_signal('quiz', ['Answer'])

        # Adding model 'Quiz'
        db.create_table('quiz_quiz', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='quizes', to=orm['auth.User'])),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('quiz', ['Quiz'])

        # Adding M2M table for field questions on 'Quiz'
        db.create_table('quiz_quiz_questions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quiz', models.ForeignKey(orm['quiz.quiz'], null=False)),
            ('question', models.ForeignKey(orm['quiz.question'], null=False))
        ))
        db.create_unique('quiz_quiz_questions', ['quiz_id', 'question_id'])

        # Adding model 'AnsweredQuestion'
        db.create_table('quiz_answeredquestion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answered_questions', to=orm['quiz.Quiz'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Question'])),
            ('selected_choice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Choice'])),
        ))
        db.send_create_signal('quiz', ['AnsweredQuestion'])

        # Adding unique constraint on 'AnsweredQuestion', fields ['quiz', 'question']
        db.create_unique('quiz_answeredquestion', ['quiz_id', 'question_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'AnsweredQuestion', fields ['quiz', 'question']
        db.delete_unique('quiz_answeredquestion', ['quiz_id', 'question_id'])

        # Deleting model 'Genre'
        db.delete_table('quiz_genre')

        # Deleting model 'Show'
        db.delete_table('quiz_show')

        # Removing M2M table for field genre on 'Show'
        db.delete_table('quiz_show_genre')

        # Deleting model 'Episode'
        db.delete_table('quiz_episode')

        # Deleting model 'Question'
        db.delete_table('quiz_question')

        # Deleting model 'Choice'
        db.delete_table('quiz_choice')

        # Deleting model 'Answer'
        db.delete_table('quiz_answer')

        # Deleting model 'Quiz'
        db.delete_table('quiz_quiz')

        # Removing M2M table for field questions on 'Quiz'
        db.delete_table('quiz_quiz_questions')

        # Deleting model 'AnsweredQuestion'
        db.delete_table('quiz_answeredquestion')


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
        'quiz.answer': {
            'Meta': {'object_name': 'Answer'},
            'choice': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answer'", 'unique': 'True', 'to': "orm['quiz.Choice']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answer'", 'unique': 'True', 'to': "orm['quiz.Question']"})
        },
        'quiz.answeredquestion': {
            'Meta': {'unique_together': "(('quiz', 'question'),)", 'object_name': 'AnsweredQuestion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quiz.Question']"}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answered_questions'", 'to': "orm['quiz.Quiz']"}),
            'selected_choice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quiz.Choice']"})
        },
        'quiz.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'choices'", 'to': "orm['quiz.Question']"})
        },
        'quiz.episode': {
            'Meta': {'object_name': 'Episode'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'episode_number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'season': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'episodes'", 'to': "orm['quiz.Show']"})
        },
        'quiz.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'quiz.question': {
            'Meta': {'object_name': 'Question'},
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quiz.Episode']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': "orm['auth.User']"}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quiz.Show']"})
        },
        'quiz.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['quiz.Question']", 'symmetrical': 'False'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quizes'", 'to': "orm['auth.User']"})
        },
        'quiz.show': {
            'Meta': {'object_name': 'Show'},
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['quiz.Genre']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['quiz']
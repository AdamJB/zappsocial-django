from django.contrib import admin
from quiz.models import Genre, Show, Episode, Question, Choice, \
    Answer, Quiz, AnsweredQuestion

# ----- Shows / Episodes ---------
class EpisodesInline(admin.TabularInline):
  model = Episode
  extra = 1

class ShowAdmin(admin.ModelAdmin):
  fields = ['title', 'genre']
  inlines = [EpisodesInline]

class EpisodeAdmin(admin.ModelAdmin):
  list_display = ('show', 'name', 'episode_number', 'season')

# ----- Quiz / Questions ---------

class AnswerInline(admin.TabularInline):
  model = Answer

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 1

class QuestionAdmin(admin.ModelAdmin):
  fields = ['owner', 'question', 'show', 'episode']
  inlines = [ChoiceInline, AnswerInline]


admin.site.register(Genre)
admin.site.register(Show, ShowAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(AnsweredQuestion)
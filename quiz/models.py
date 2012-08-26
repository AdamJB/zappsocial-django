from django.contrib.auth.models import User
from django.db import models

class Genre(models.Model):
  name = models.CharField(max_length=255, unique=True)

  def __unicode__(self):
    return self.name

class Show(models.Model):
  title = models.CharField(max_length=255, help_text="TV Show/Film")
  genre = models.ManyToManyField(Genre)

  def __unicode__(self):
    return self.title

class Episode(models.Model):
  show = models.ForeignKey(Show, related_name="episodes")
  name = models.CharField(max_length=255)
  episode_number = models.IntegerField(blank=True, default=0)
  season = models.IntegerField(blank=True, default=0)
  description = models.CharField(max_length=255, blank=True)

  def __unicode__(self):
    return "%s - Episode %d" % (self.show, self.episode_number)

class Question(models.Model):
  owner = models.ForeignKey(User, related_name="questions")
  question = models.CharField(max_length=1024, blank=False)
  show = models.ForeignKey(Show)
  episode = models.ForeignKey(Episode, blank=True)

  def __unicode__(self):
    return self.question

class Choice(models.Model):
  choice = models.CharField(max_length=1024, blank=False)
  question = models.ForeignKey(Question, related_name="choices")

  def __unicode__(self):
    return "%s - %s" % (self.question.question, self.choice)

class Answer(models.Model):
  question = models.ForeignKey(Question, related_name="answer", unique=True)
  choice = models.ForeignKey(Choice, related_name="answer", unique=True)

  def __unicode__(self):
    return "%s - %s" % (self.question.question, self.choice.choice)

class Quiz(models.Model):
  user = models.ForeignKey(User, related_name="quizes")
  # A Quiz Generator must be created, where user passes the Tags/Category
  questions = models.ManyToManyField(Question)
  score = models.IntegerField(blank=True, default=0)

  class Meta:
    verbose_name_plural = "quizes"

class AnsweredQuestion(models.Model):
  quiz = models.ForeignKey(Quiz, related_name="answered_questions")
  question = models.ForeignKey(Question)
  selected_choice = models.ForeignKey(Choice)

  class Meta:
    unique_together = ('quiz', 'question')

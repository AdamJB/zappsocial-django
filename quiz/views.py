from django.template import Context, loader
from django.http import HttpResponse
from models import *

# TOOD: Move this to a subfolder views/quiz.py

def index(request):
  shows_list = Show.objects.all().order_by('title')
  template = loader.get_template('quiz/index.html')
  c = Context({
      'shows_list': shows_list,
  })
  return HttpResponse(template.render(c))

# TOOD: (These are generic stubs)

def generate(request, quiz_type, id):
  #TODO: quizGeneration Logic
  if quiz_type == "show":
    show = Show.objects.all().filter(pk=id)
    if show:
      return HttpResponse("Generate Show quiz for: %s " % show[0].title)
    else:
      return HttpResponse("Invalid show to create quiz for")
  #TODO: Can only have active 1 quiz per show/genre at a time?
  return HttpResponse("Can't generate a quiz with no info")

def detail(request, quiz_id):
  return HttpResponse("Start Quiz? / Results / Current Quizes")

def question(request, quiz_id, question_id):
  return HttpResponse("Answer This question? / Answered already?")
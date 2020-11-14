from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Score
from .models import Course
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ScoreForm


# Create your views here.

class CourseCreate(CreateView):
    model = Course
    fields = "__all__"

class CourseDelete(DeleteView):
  model = Course
  success_url = "/course/"

class CourseUpdate(UpdateView):
  model = Course
  fields = "__all__"


class ScoreCreate(CreateView):
  model = Score
  fields = "__all__"

class ScoreDelete(DeleteView):
  model = Score
  success_url = "/scores/"

class ScoreUpdate(UpdateView):
  model = Score
  fields = "__all__"


def home(request):
    return render(request, "about.html")

def analytics(request):
  return render(request, "analytics.html")
    
def score_index(request):
    score = Score.objects.all()
    return render(request, 'score/index.html', {'score': score})

def course_index(request):
    course = Course.objects.all()
    return render(request, 'course/index.html', {'course': course})

# def course_detail(request, course_id):
#     courses = Course.objects.get(id=course_id)
#     return render(request, 'course/detail.html', {'courses': courses,})

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    score_sets = course.score_set.all()
    score_form = ScoreForm()
    return render(request, 'course/detail.html',
    {'course': course, 'score_form': score_form})

def add_score(request, course_id):
      # create a ModelForm instance using the data in request.POST
  form = ScoreForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_score = form.save(commit=False)
    new_score.course_id = course_id
    new_score.save()
  return redirect('detail', course_id=course_id)


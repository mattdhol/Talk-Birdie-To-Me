from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Score
from .models import Course
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ScoreForm
# from .forms import CourseForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

class CourseCreate(LoginRequiredMixin, CreateView):
    model = Course
    fields = "__all__"

    def form_valid(self, form):
          # Assign the logged in user (self.request.user)
      form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
      return super().form_valid(form)

class CourseDelete(LoginRequiredMixin, DeleteView):
  model = Course
  success_url = "/course/"

class CourseUpdate(LoginRequiredMixin, UpdateView):
  model = Course
  fields = "__all__"


class ScoreCreate(LoginRequiredMixin, CreateView):
  model = Score
  fields = "__all__"

  def form_valid(self, form):
  # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
  # Let the CreateView do its job as usual
    return super().form_valid(form)




class ScoreDelete(LoginRequiredMixin, DeleteView):
  model = Score
  success_url = "/scores/"

class ScoreUpdate(LoginRequiredMixin, UpdateView):
  model = Score
  fields = "__all__"


def home(request):
    return render(request, "about.html")

def analytics(request):
  return render(request, "analytics.html")

@login_required
def score_index(request):
    score = Score.objects.all()
    # score = Score.objects.filter(user=request.user)
    return render(request, 'score/index.html', {'score': score})

@login_required
def course_index(request):
    course = Course.objects.filter(user=request.user)
    return render(request, 'course/index.html', {'course': course})

@login_required
def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    score_sets = course.score_set.all()
    score_form = ScoreForm()
    return render(request, 'course/detail.html',
    {'course': course, 'score_form': score_form})

@login_required
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = { 'form': form, 'error_message': error_message }
  return render(request, 'registration/signup.html', context)
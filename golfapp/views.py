from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Score
from .models import Course
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ScoreForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  TemplateView
from django.views.generic import View
import operator
from django.db.models import Avg, Max, Min, Sum
from django.contrib.auth.models import User

class ScoreChart(TemplateView):  
  template_name = 'analytics/chart.html'
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    current_user_score = Score.objects.filter(user=self.request.user)
    context["qs"] = current_user_score
    allscore = Score.objects.all()

    score_ave = current_user_score.aggregate(Avg('total_score'))
    score_ave['total_score__avg'] = round(score_ave['total_score__avg'],2)
    context["score_ave"] = score_ave['total_score__avg']

    score_best = current_user_score.aggregate(Min('total_score'))
    context["score_best"] = score_best['total_score__min']

    total_strokes = current_user_score.aggregate(Sum('total_score'))
    context["total_strokes"] = total_strokes['total_score__sum']

    last_five = current_user_score.filter().order_by('-date')[:5]

    avg_last_five = last_five.aggregate(Avg('total_score'))
    context["avg_last_five"] = avg_last_five['total_score__avg']

    last_five_lowest = last_five.aggregate(Min('total_score'))
    context["last_five_lowest"] = last_five_lowest['total_score__min']

    last_five_strokes = last_five.aggregate(Sum('total_score'))
    context["last_five_strokes"] = last_five_strokes['total_score__sum']
    return context

class ScoreChartBreak(TemplateView):
  template_name = 'analytics/break.html'
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    current_user_score = Score.objects.filter(user=self.request.user)
    context["qs"] = current_user_score
    allscore = Score.objects.all()

    par_ave = current_user_score.aggregate(Avg('number_of_pars'))
    par_ave['number_of_pars__avg'] = round(par_ave['number_of_pars__avg'],2)
    context["par_ave"] = par_ave['number_of_pars__avg']

    par_max = current_user_score.aggregate(Max('number_of_pars'))
    context["par_max"] = par_max['number_of_pars__max']

    par_total = current_user_score.aggregate(Sum('number_of_pars'))
    context["par_total"] = par_total['number_of_pars__sum']


    birdie_ave = current_user_score.aggregate(Avg('number_of_birdies'))
    birdie_ave['number_of_birdies__avg'] = round(birdie_ave['number_of_birdies__avg'],2)
    context["birdie_ave"] = birdie_ave['number_of_birdies__avg']

    birdie_max = current_user_score.aggregate(Max('number_of_birdies'))
    context["birdie_max"] = birdie_max['number_of_birdies__max']

    birdie_total = current_user_score.aggregate(Sum('number_of_birdies'))
    context["birdie_total"] = birdie_total['number_of_birdies__sum']

    greens_hit = current_user_score.aggregate(Avg('number_of_greens_hit'))
    greens_hit['number_of_greens_hit__avg'] = round(greens_hit['number_of_greens_hit__avg'],2)
    context["greens_hit_ave"] = greens_hit['number_of_greens_hit__avg']


    greens_hit_max = current_user_score.aggregate(Max('number_of_greens_hit'))
    context["greens_hit_max"] = greens_hit_max['number_of_greens_hit__max']

    greens_hit_total = current_user_score.aggregate(Sum('number_of_greens_hit'))
    context["greens_hit_total"] = greens_hit_total['number_of_greens_hit__sum']

    fairways_hit = current_user_score.aggregate(Avg('number_of_fairways_hit'))
    fairways_hit['number_of_fairways_hit__avg'] = round(fairways_hit['number_of_fairways_hit__avg'],2)
    context["fairways_hit_ave"] = fairways_hit['number_of_fairways_hit__avg']

    fairways_hit_max = current_user_score.aggregate(Max('number_of_fairways_hit'))
    context["fairways_hit_max"] = fairways_hit_max['number_of_fairways_hit__max']

    fairways_hit_total = current_user_score.aggregate(Sum('number_of_fairways_hit'))
    context["fairways_hit_total"] = fairways_hit_total['number_of_fairways_hit__sum']


    last_five = current_user_score.filter().order_by('-date')[:5]

    last_five_birdie_avg = last_five.aggregate(Avg('number_of_birdies'))
    context["last_five_birdie_avg"] = (last_five_birdie_avg['number_of_birdies__avg'])


    birdie_five_most = last_five.aggregate(Max('number_of_birdies'))
    context["birdie_five_most"] = (birdie_five_most['number_of_birdies__max'])

    last_five_birdie_sum = last_five.aggregate(Sum('number_of_birdies'))
    context["last_five_birdie_sum"] = (last_five_birdie_sum['number_of_birdies__sum'])


    last_five_par_avg = last_five.aggregate(Avg('number_of_pars'))
    context["last_five_par_avg"] = (last_five_par_avg['number_of_pars__avg'])

    last_five_par_max = last_five.aggregate(Max('number_of_pars'))
    context["last_five_par_max"] = (last_five_par_max['number_of_pars__max'])

    last_five_par_sum = last_five.aggregate(Sum('number_of_pars'))
    context["last_five_par_sum"] = (last_five_par_sum['number_of_pars__sum'])

    last_five_fairway_avg = last_five.aggregate(Avg('number_of_fairways_hit'))
    context["last_five_fairway_avg"] = (last_five_fairway_avg['number_of_fairways_hit__avg'])

    last_five_fairway_max = last_five.aggregate(Max('number_of_fairways_hit'))
    context["last_five_fairway_max"] = (last_five_fairway_max['number_of_fairways_hit__max'])

    last_five_fairway_sum = last_five.aggregate(Sum('number_of_fairways_hit'))
    context["last_five_fairway_sum"] = (last_five_fairway_sum['number_of_fairways_hit__sum'])  

    last_five_green_avg = last_five.aggregate(Avg('number_of_greens_hit'))
    context["last_five_green_avg"] = (last_five_green_avg['number_of_greens_hit__avg'])

    last_five_green_max = last_five.aggregate(Max('number_of_greens_hit'))
    context["last_five_green_max"] = (last_five_green_max['number_of_greens_hit__max'])

    last_five_greens_sum = last_five.aggregate(Sum('number_of_greens_hit'))
    context["last_five_greens_sum"] = (last_five_greens_sum['number_of_greens_hit__sum'])   
    return context

    
class CourseCreate(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['course_name', 'par', 'things_to_remember']
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
  fields = ['course_name', 'par', 'things_to_remember']

class ScoreCreate(LoginRequiredMixin, CreateView):
  model = Score
  fields = ['date', 'total_score', 'number_of_birdies', 'number_of_pars', 'number_of_fairways_hit', 'number_of_greens_hit', 'memorable_moment']
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
    score = Score.objects.filter(user=request.user)
    return render(request, 'score/index.html', {'score': score})

@login_required
def course_index(request):
    course = Course.objects.filter(user=request.user)
    tmp = sorted(course, key = operator.attrgetter('course_name'))
    course = tmp
    # counter = 0
    # sum = 0
    # for c in course:
    #   print(c.course_name)
    #   for score in c.score_set.all():
    #     sum = int(sum) + int(score)
    #     counter += 1
    # avg = sum / counter
    # print(avg)
      # course_scores = [{'braeben' : 80}, {'asdf': 90}]  
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
  print(request.user.id)
  form = ScoreForm(request.POST)
  if form.is_valid():
    new_score = form.save(commit=False)
    new_score.course_id = course_id
    user = User.objects.get(id=request.user.id)
    new_score.user = user
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
from django.urls import path
from . import views
from .models import Course, Score  
from django.views.generic import  TemplateView
from golfapp.views import ScoreChart
from golfapp.views import ScoreChartBreak

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),

  path('analytics/', ScoreChart.as_view(), name='analytics'),
  path('analytics/breakdown/', ScoreChartBreak.as_view(), name='break'),

  path('course/', views.course_index, name='course_index'),
  path('course/create', views.CourseCreate.as_view(), name='course_create'),
  path('course/<int:pk>/delete/', views.CourseDelete.as_view(), name='course_delete'),
  path('course/<int:pk>/update/', views.CourseUpdate.as_view(), name='course_update'),
  path('course/<int:course_id>/', views.course_detail, name='detail'),
  path('course/<int:course_id>/add_score/', views.add_score, name='add_score'),
  
  path('scores/', views.score_index, name='index'),
  path('scores/create', views.ScoreCreate.as_view(), name='score_create'),
  path('scores/<int:pk>/delete/', views.ScoreDelete.as_view(), name='score_delete'),
  path('scores/<int:pk>/update/', views.ScoreUpdate.as_view(), name='score_update'),
]



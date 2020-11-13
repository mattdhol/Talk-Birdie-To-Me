from django.urls import path
from . import views
from .models import Course, Score


urlpatterns = [
  path('', views.home, name='home'),

  path('scores/', views.score_index, name='index'),
  path('scores/create', views.ScoreCreate.as_view(), name='score_create'),

  path('course/', views.course_index, name='course_index'),
  path('course/create', views.CourseCreate.as_view(), name='course_create'),

  path('course/<int:course_id>/', views.course_detail, name='detail'),

  path('course/<int:course_id>/add_score/', views.add_score, name='add_score'),
]



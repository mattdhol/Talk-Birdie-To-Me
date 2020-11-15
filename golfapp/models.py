from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    par = models.IntegerField()
    things_to_remember = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, default='0', on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return "/course/"

class Score(models.Model):
    date = models.DateField()
    total_score = models.IntegerField()
    number_of_eagles = models.IntegerField(default=0)
    number_of_birdies = models.IntegerField(default=0)
    number_of_pars = models.IntegerField(default=0)
    number_of_bogeys = models.IntegerField(default=0)
    number_of_blow_up_holes = models.IntegerField(default=0)
    number_of_fairways_hit = models.IntegerField(default=0)
    number_of_greens_hit = models.IntegerField(default=0)
    memorable_moment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    
    def __int__(self):
        return self.total_score

    def get_absolute_url(self):
        return "/scores/"



    # def __str__(self):
    #     return f"{self.get_drink_display()} on {self.date}"
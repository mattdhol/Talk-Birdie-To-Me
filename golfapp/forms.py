from django.forms import ModelForm, HiddenInput
from .models import Score
from .models import Course

class ScoreForm(ModelForm):
  class Meta:
    model = Score
    fields = ['date', 'total_score', 'number_of_birdies', 'number_of_pars',
     'number_of_fairways_hit', 'number_of_greens_hit', 'memorable_moment']


from django import forms

from .models import Results

class ResultForm(forms.ModelForm):
    class Meta:
        model = Results
        fields = ('home_team', 'away_team', 'home_goals', 'away_goals', 'round', )
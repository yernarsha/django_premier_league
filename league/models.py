from django.db import models

# Create your models here.

class Teams(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Results(models.Model):
    home_team = models.ForeignKey(Teams, related_name='home_team', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Teams, related_name='away_team', on_delete=models.CASCADE)
    home_goals = models.PositiveIntegerField(default=0) # must be either positive or zero (0)
    away_goals = models.PositiveIntegerField(default=0)
    round = models.PositiveIntegerField(default=1)


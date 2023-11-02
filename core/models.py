from django.db import models

# Create your models here.
class FootballTeam(models.Model):
    team_name = models.CharField(max_length=200)
    team_city = models.CharField(max_length=200)
    win = models.BooleanField(default=False)
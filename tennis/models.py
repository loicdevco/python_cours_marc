import datetime
from django.db import models

class Ligue(models.Model) : 
    nom_ligue = models.CharField(max_length=200)
    def __str__(self):
        return self.nom_ligue

class Participant(models.Model):
    nom_participant = models.CharField(max_length=200)
    prenom_participant = models.CharField(max_length=200)
    ligue = models.ForeignKey(Ligue, default = "", on_delete=models.CASCADE)
    def __str__(self):
        return self.nom_participant

class Match(models.Model):
    nom_match = models.CharField(max_length=200)
    date_match = models.DateField(default=datetime.date.today)
    participant = models.ForeignKey(Participant, default = "", on_delete=models.CASCADE)
    score = models.IntegerField()
    def __str__(self):
        return self.nom_match


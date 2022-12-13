from django.forms import ModelForm

from .models import Participant, Ligue

class ParticipantForm(ModelForm):

    class Meta:
        model = Participant
        fields = ["nom_participant",
				  "prenom_participant",
                  "ligue"
				]

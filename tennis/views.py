import random
from django.forms import formset_factory
from django.shortcuts import render, redirect

from .models import Participant, Ligue
from .forms import ParticipantForm


def index(request):
    form = ParticipantForm()
    # verification de la methode http
    if request.method == "POST":
        # Instancier le formulaire
        form = ParticipantForm(request.POST)
        # tester le validité du formulaire
        if form.is_valid():
            # enregistrer les données
            form.save()
            # rediriger vers l'index
            return redirect("tennis:index")
    participant_list = Participant.objects.all()
    ligue_list = Ligue.objects.all()
    return render(request, "index.html", {"participant_list": participant_list, "participant_form": form, "ligue_list": ligue_list})

def update(request, pk):
	participant = Participant.objects.get(id = pk)
	form = ParticipantForm(instance=participant)
	if request.method == "POST":
		form = ParticipantForm(request.POST, instance=participant)
		if form.is_valid():
			form.save()
			return redirect("tennis:index")
	return render(request, "update.html", {"edit_participant_form": form})

def delete(request, pk):
	participant = Participant.objects.get(id = pk)
	if request.method == "POST":
		participant.delete()
		return redirect("tennis:index")
	return render(request,"delete.html",{"participant":participant})

def player_pairs(array):
    results = []
    for i in range(0, len(array) - 1):
        for j in range(i+1, len(array)):
            results.append(array[i] + array[j])
    return results

def classement(array):
    score_classer = sorted(array)
    return score_classer

def match(request, pk) :
    list_perso = list(Participant.objects.filter(id = pk).values('nom_participant'))
    list_other = list(Participant.objects.exclude(id =pk).values('nom_participant'))
    match_tab = list(zip(list_other, list_perso))[0]

    participant_final_perso = list(list_perso)
    participant_final_other = list(list_other)
    score = [0, 1, 2, 3, 4, 5, 6, 7]
    scorebis = [7, 6, 5, 4, 3, 2, 1, 0]
    score1 = random.choice(score)
    score2 = random.choice(scorebis)

    return render(request,"match.html", {"match_tab":match_tab, "score1":score1, "score2":score2, "participant_final_perso":participant_final_perso, "participant_final_other":participant_final_other})

       
    

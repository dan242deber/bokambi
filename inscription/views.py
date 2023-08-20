from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from inscription.models import *



def Enrolle(request):
    template = loader.get_template('enrolle_agent.html')
    return HttpResponse(template.render())


def candidature_liste(request):
    candidatures = Candidature.objects.all()
    return render(request, 'candidature.html', {'candidatures': candidatures})

def candidater(request):
    id_cand = request.GET.get('id_cand')
    return render(request,'candidater.html',{'id_cand':id_cand})


def enregistrement(request):
    nom=request.POST.get('nom_pers')
    prenom=request.POST.get('prenom_pers')
    date_nais=request.POST.get('date_nais_pers')
    pays=request.POST.get('pays_nais_pers')
    ville=request.POST.get('ville_nais_pers')
    adresse=request.POST.get('adresse_pers')
    telephone=request.POST.get('telephone_pers')
    email=request.POST.get('email_pers')
    genre=request.POST.get('genre_pers')
    dossier=request.POST.get('dossier_cand_pers')
    id_candidature=request.POST.get('id_cand')
    id_cand_inst=Candidature.objects.get(id_cand=id_candidature)
    if request.method == 'POST':
        personne=Personne(
            nom_pers=nom,
            prenom_pers=prenom,
            date_nais_pers=date_nais,
            pays_nais_pers=pays,
            ville_nais_pers=ville,
            adresse_pers=adresse,
            telephone_pers=telephone,
            email_pers=email,
            genre_pers=genre,
            dossier_cand_pers=dossier,
            id_cand=id_cand_inst
        )
        # personne.id_cand=1
        personne.save()

        
    else:
        pass
    return render(request,'candidater.html',{'id_cand':2})
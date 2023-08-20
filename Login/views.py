from django.utils import timezone
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout,login
from django.contrib.sessions.models import Session
from Login.fonc_login import calculer_age, get_online_users
from inscription.models import *
from django.shortcuts import render
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from .models import AgentPublic
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta
from .models import AgentPublic
from collections import defaultdict
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io
from django.db.models import Q
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.core.mail import send_mail









def forget(request):
    return render(request,'oublier.html')

def send_email_to_agent(request):

    try:
        agent=AgentPublic.objects.get(email_ag_pb=request.POST.get('username'))
        mot_de_passe=agent.pass_ag_pb
        send_mail(
                subject="Message important",
                message=f"Votre mot de passe est : {mot_de_passe}",
                from_email="cgdan.2000@gmail.com",
                recipient_list=[agent.email_ag_pb],
            )
        response = "Message envoyé avec succès à l'agent."
        return render(request,'login.html')
    except Exception as e:
        print("Erreur lors de l'envoi de l'e-mail:", e)
        response = "Une erreur est survenue lors de l'envoi du message."

    return HttpResponse(response)



























def histogramme(request):
    # Get the data
    data = {
        2022: 0,
        2023: 0,
        2024: 0,
        2025: 0,
        2026: 1,
        2027: 0,
        2028: 0,
        2029: 0,
        2030: 0,
        2031: 0,
        2032: 0,
    }

    # Create the figure
    fig, ax = plt.subplots()
    ax.hist(data.values(), bins=10)
    ax.set_title("Histogramme des retraies 10 prochaines années")
    ax.set_xlabel("Nombre de retraités ")
    ax.set_ylabel("Année")

    # Convert the figure to base64
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode("utf-8")

    return render(request, 'statistique.html', {'image_base64': image_base64})






def statistiques(request):
    # Calculez la date de début et de fin de la période souhaitée
    try:
        jour=request.jour
    except:
        jour=30

    date_debut = datetime.now() - timedelta(days=jour)  # Par exemple, les 30 derniers jours
    date_fin = datetime.now()

    # Obtenez le nombre d'agents nommés par genre dans la période donnée
    agents = AgentPublic.objects.filter(date_nomination_ag_pb__range=(date_debut, date_fin))
    genres = agents.values_list('genre_ag_pb', flat=True)
    counts = {'M': 0, 'F': 0}
    for genre in genres:
        counts[genre] += 1

    # Créez un graphique camembert (pie chart)
    labels = ['Masculin', 'Féminin']
    sizes = [counts['M'], counts['F']]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

    # Convertissez le graphique en image
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()

    context = {
        'image_base64': image_base64,
        'date_debut': date_debut,
        'date_fin': date_fin,
    }

    return render(request, 'agent_actif.html', context)




def Login(request):
    return render(request,'login.html')

def IndexL(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def ajout_ag_pub(request):
    cand=Candidature.objects.all()
    return render(request,'pages/Ajouter-agent-fonct.html',{'candidature':cand})

def enreg_ag_pub(request):
    nom=request.POST.get('nom_ag_pb')
    prenom=request.POST.get('prenom_ag_pb')
    date_nais=request.POST.get('date_nais_ag_pb')
    pays=request.POST.get('pays_nais_ag_pb')
    ville=request.POST.get('ville_nais_ag_pb')
    adresse=request.POST.get('adresse_ag_pb')
    telephone=request.POST.get('telephone_ag_pb')
    email=request.POST.get('email_ag_pb')
    genre=request.POST.get('genre_ag_pb')
    pass_ag=request.POST.get('pass_ag_pb')


    id_candidature=request.POST.get('id_cand')
    id_cand_inst=Candidature.objects.get(id_cand=id_candidature)
    if request.method =='POST':
        agent_pub=AgentPublic(
            nom_ag_pb=nom,
            prenom_ag_pb=prenom,
            date_nais_ag_pb=date_nais,
            pays_nais_ag_pb=pays,
            ville_nais_ag_pb=ville,
            date_nomination_ag_pb=timezone.now(),
            adresse_ag_pb=adresse,
            telephone_ag_pb=telephone,
            email_ag_pb=email,
            statut_ag_pb="Actif",
            genre_ag_pb=genre,
            id_cand=id_cand_inst,
            pass_ag_pb=pass_ag,
        )
        agent_pub.save()
        
        
        return render(request,'pages/Ajouter-agent-fonct.html')
        
    else:
        return render(request,'pages/Ajouter-agent-fonct.html')
        

def modif_ag_pub(request):
    agents=AgentPublic.objects.all()
    
    return render(request,'pages/modifier-agent.html',{'agents':agents})


def enr_modif_ag_pub(request):

    email = request.POST.get('email_ag_pb')
    nom_nouveau = request.POST.get('nom_ag_pb')
    prenom_nouveau = request.POST.get('prenom_ag_pb')
    adresse = request.POST.get('adresse_ag_pb')
    telephone = request.POST.get('telephone_ag_pb')

    try:
        agent = AgentPublic.objects.get(email_ag_pb=email)
        agent.nom_ag_pb = nom_nouveau
        agent.prenom_ag_pb = prenom_nouveau
        agent.adresse_ag_pb = adresse
        agent.telephone_ag_pb = telephone
        agent.email_ag_pb = email
        agent.save()
        message = "Nom de l'agent mis à jour avec succès."
    except AgentPublic.DoesNotExist:
        message = "Agent non trouvé."
    agents=AgentPublic.objects.all()

    return render(request, 'pages/modifier-agent.html', {'agents':agents,'message': message})
    



def info_update(request):
    email = request.POST.get('email_ag_pb')
    id = request.POST.get('agent')
    pass_ag = request.POST.get('pass_ag_pb')
    try:
        agent = AgentPublic.objects.get(id_ag_pb=id)
        agent.email_ag_pb = email
        agent.pass_ag_pb = pass_ag
        agent.save()
        message = "Nom de l'agent mis à jour avec succès."
    except AgentPublic.DoesNotExist:
        message = "Agent non trouvé."
    agents=AgentPublic.objects.all()
    return render(request,'pages/Ajouter-agent-fonct.html')

def mes_info(request):
    ag_info=request.POST.get('l')
    agent=AgentPublic.objects.get(id_ag_pb=ag_info)
    return render(request,'pages/mes_info.html',{'courant_user':agent})




def Connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        agent_pub = AgentPublic.objects.filter(email_ag_pb=username).first()
        nb_actif=AgentPublic.objects.filter(statut_ag_pb="Actif").count()
        nb_re=AgentPublic.objects.filter(statut_ag_pb="Retraité").count()
        if agent_pub.pass_ag_pb==password:
         #   login(request, agent_pub)
            return render(request,'Admin_Dashboard_Index.html',{'agent':agent_pub,"nb_actif":nb_actif,"nb_re":nb_re})

    

    return render(request, 'login.html',{'id':agent_pub})



def supprimer(request):
    agents=AgentPublic.objects.all()
    
    return render(request,'pages/supprimer.html',{'agents':agents})

def supprimer_def(request):
    email = request.POST.get('email_ag_pb')
    id = request.POST.get('agent')
    pass_ag = request.POST.get('pass_ag_pb')
    agent = AgentPublic.objects.get(id_ag_pb=id)
    agent.statut_ag_pb="Radié"
    agent.save()
    message = "Nom de l'agent mis à jour avec succès."
    message = "Agent non trouvé."
    agents=AgentPublic.objects.all()
    return render(request,'pages/Ajouter-agent-fonct.html')



def Connexion2(request):
    # agent_pub = AgentPublic.objects.filter(email_ag_pb=username).first()
    # nb_actif=AgentPublic.objects.filter(statut_ag_pb="Actif").count()
    # nb_re=AgentPublic.objects.filter(statut_ag_pb="Retraité").count()
    # return render(request,'Admin_Dashboard_Index.html',{'agent':agent_pub,"nb_actif":nb_actif,"nb_re":nb_re})
    pass


def ajout_cand(request):
    departement=Departement.objects.all()
    poste_t=PosteTravail.objects.all()
    ministere=Ministere.objects.all()

    return render(
        request,
        'ajout_cand.html',
        {
            'departement':departement,
            'poste_t':poste_t,
            'ministere':ministere
        }
    )


def ajout_cand_save(request):
    lib_can=request.POST.get('lib_cand')

    id_dep=request.POST.get('id_depart')
    id_depart_inst=Departement.objects.get(id_depart=id_dep)

    id_post=request.POST.get('id_post_trav')
    id_post_inst=PosteTravail.objects.get(id_post_trav=id_post)

    cle_mini=request.POST.get('id_ministere')
    id_min=Ministere.objects.get(id_ministere=cle_mini)

    if request.method =='POST':
        candidature=Candidature(
            lib_cand=lib_can,
            date_cand=datetime.now(),
            id_depart=id_depart_inst,
            id_post_trav=id_post_inst,
            id_ministere=id_min
        )
        candidature.save()
        


    return render(request,'Admin_Dashboard_Index.html',{'agent':agent_pub,"nb_actif":nb_actif,"nb_re":nb_re})

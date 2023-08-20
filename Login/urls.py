from django.urls import path
from . import views

urlpatterns = [
    path('Login', views.Login, name='Login'),
    path('', views.IndexL, name='IndexL'),
    path('Drashboard', views.Connexion, name='Connexion'),
    path('Drashboard/ajout-agent', views.ajout_ag_pub, name='ajout_ag_pub'),
    path('Drashboard/ajout-agen', views.enreg_ag_pub, name='enreg_ag_pub'),
    path('Drashboard/modifier', views.modif_ag_pub, name='modif_ag_pub'),
    path('Drashboard/supprimer', views.supprimer, name='supprimer'),
    path('Drashboard/supprimerdef', views.supprimer_def, name='supprimer_def'),
    path('Drashboard/stat', views.statistiques, name='statistiques'),
    path('Drashboard/stat2', views.histogramme, name='histogramme'),
    path('Drashboard/profils', views.mes_info, name='mes_info'),
    path('Drashboard/mod', views.enr_modif_ag_pub, name='enr_modif_ag_pub'),
    path('Drashboard/', views.info_update, name='info_update'),
    path('Oublier/', views.forget, name='forget'),
    path('Login/', views.send_email_to_agent, name='send_email_to_agent'),
    path('Drashboard/cand_aj', views.ajout_cand, name='ajout_cand'),
    path('cand_aj2', views.ajout_cand_save, name='ajout_cand_save'),
  
]
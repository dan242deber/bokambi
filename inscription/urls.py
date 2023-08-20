import statistics
from django.urls import path

from Bokambi_ya_basali import settings
from . import views

urlpatterns = [
    path('inscr', views.Enrolle, name='Enrolle'),
    path('candidature',views.candidature_liste,name='candidature'),
    path('candidater',views.candidater,name='candidater'),
    path('enregistrement',views.enregistrement,name='enregistrement'),
]


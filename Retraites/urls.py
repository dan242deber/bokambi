from django.urls import path
from . import views

urlpatterns = [
    # path('Retraites', views.Retraites, name='Retraites'),
    path('IndexR', views.IndexR, name='IndexR'),

]
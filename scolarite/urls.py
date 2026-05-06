from django.urls import path
from . import views

urlpatterns = [
        path('', views.page_accueil, name='accueil'),
        path('admin-absences/', views.ajouter_absence, name='ajouter_absence'),
        path('mes-absences/', views.liste_absences_etudiant, name='mes_absences'),

]
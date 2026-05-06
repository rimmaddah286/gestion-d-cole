from django.contrib import admin
from .models import Profil

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    # Les colonnes qui s'afficheront dans la liste
    list_display = ('user', 'role', 'telephone')
    
    # Ajouter un filtre sur le côté pour trier par rôle (Admin/Prof/Etudiant)
    list_filter = ('role',)
    
    # Ajouter une barre de recherche pour trouver un utilisateur par son nom
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'telephone')
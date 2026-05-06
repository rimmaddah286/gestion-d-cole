from django.contrib import admin
from .models import Filiere, Matiere
from .models import Filiere, Matiere, Etudiant, Professeur

@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    list_display = ('code', 'nom')
    search_fields = ('nom', 'code')

@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'filiere', 'coefficient')
    list_filter = ('filiere',) # Pratique pour voir les matières par filière




@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('profil', 'filiere', 'date_inscription')
    list_filter = ('filiere',)

@admin.register(Professeur)
class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ('profil', 'specialite')
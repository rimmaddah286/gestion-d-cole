from django.db import models
from authentification.models import Profil # Import du profil pour le lien
from django.contrib.auth.models import User


class Filiere(models.Model):
    nom = models.CharField(max_length=100) # ex: Génie Informatique
    code = models.CharField(max_length=10, unique=True) # ex: GI

    def __str__(self):
        return self.nom

class Matiere(models.Model):
    libelle = models.CharField(max_length=100)
    coefficient = models.IntegerField(default=1)
    # Relation : Une matière appartient à une filière
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, related_name='matieres')

    def __str__(self):
        return f"{self.libelle} ({self.filiere.code})"
    


class Etudiant(models.Model):
    # Lien vers le profil (qui lui-même est lié à User)
    profil = models.OneToOneField(Profil, on_delete=models.CASCADE, related_name='etudiant_data')
    # Lien vers sa filière
    filiere = models.ForeignKey(Filiere, on_delete=models.SET_NULL, null=True, related_name='etudiants')
    date_inscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Étudiant : {self.profil.user.last_name} {self.profil.user.first_name}"

class Professeur(models.Model):
    profil = models.OneToOneField(Profil, on_delete=models.CASCADE, related_name='professeur_data')
    # Un professeur peut enseigner plusieurs matières
    matieres = models.ManyToManyField(Matiere, related_name='professeurs')
    specialite = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Pr. {self.profil.user.last_name}"
    


class Absence(models.Model):
    # On lie l'absence à l'étudiant via son profil
    etudiant = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    seance = models.CharField(max_length=50) # Ex: "08:30 - 10:30"
    matiere = models.CharField(max_length=100)
    justifiee = models.BooleanField(default=False)


class SeanceCours(models.Model):
    JOURS = [
        ('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi'), ('Samedi', 'Samedi'),
    ]
    matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE)
    jour = models.CharField(max_length=10, choices=JOURS)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    salle = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.matiere.libelle} - {self.jour} ({self.heure_debut})"
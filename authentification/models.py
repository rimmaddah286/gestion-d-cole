
from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    # Relier ce profil à l'utilisateur par défaut de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')


    CHOIX_ROLES = (
        ('ADMIN', 'Administrateur'),
        ('PROF', 'Professeur'),
        ('ETUDIANT', 'Étudiant'),
    )
    role = models.CharField(max_length=10, choices=CHOIX_ROLES)
    telephone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

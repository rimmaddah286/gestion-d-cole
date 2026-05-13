from django.shortcuts import render, redirect # Ajout de redirect ici
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Filiere, Etudiant, Professeur, Absence, SeanceCours

@login_required
def page_accueil(request):
    # .strip() enlève les espaces, .upper() met tout en majuscules
    role = request.user.profil.role.strip().upper() 
    
    print(f"DEBUG: Le rôle détecté est [{role}]")

    if role == 'ETUDIANT':
        # On récupère les données AVANT de faire le return
        absences = Absence.objects.filter(etudiant=request.user)
        count = absences.count()
        return render(request, 'scolarite/accueil_etudiant.html', {
            'absences': absences, 
            'count': count
        })
        
    elif role == 'PROF':
        return render(request, 'scolarite/accueil_prof.html')
    
    else:
        # Accueil pour l'ADMIN
        return render(request, 'scolarite/accueil_admin.html')

def ajouter_absence(request):
    # Vérification de sécurité pour l'admin
    if request.user.profil.role.upper() != 'ADMIN' and not request.user.is_staff:
        return redirect('page_accueil')

    if request.method == 'POST':
        etudiant_id = request.POST.get('etudiant')
        matiere = request.POST.get('matiere')
        seance = request.POST.get('seance')
        
        Absence.objects.create(
            etudiant_id=etudiant_id,
            matiere=matiere,
            seance=seance
        )
        return redirect('page_accueil')

    etudiants = User.objects.filter(profil__role='ETUDIANT')
    return render(request, 'scolarite/admin_absences.html', {'etudiants': etudiants})

@login_required
def liste_absences_etudiant(request):
    # On récupère les absences de l'étudiant connecté
    absences = Absence.objects.filter(etudiant=request.user).order_by('-date')
    count = absences.count()
    
    return render(request, 'scolarite/consultation_absences.html', {
        'absences': absences,
        'count': count
    })

def voir_emploi_du_temps(request):
    # Cette vue récupère tout ce que l'admin a rempli dans SeanceCours
    emplois = SeanceCours.objects.all().order_by('heure_debut')
    return render(request, 'scolarite/planning.html', {'emplois': emplois})
from django.shortcuts import render
from django.contrib.auth.decorators import login_required # Import du décorateur
from .models import Filiere, Etudiant, Professeur
from .models import Absence
from django.contrib.auth.models import User

@login_required
def page_accueil(request):
    # .strip() enlève les espaces, .upper() met tout en majuscules
    role = request.user.profil.role.strip().upper() 
    
    print(f"DEBUG: Le rôle détecté est [{role}]") # Regarde ton terminal pour voir ça

    if role == 'ETUDIANT':
        return render(request, 'scolarite/accueil_etudiant.html')
        # Dans views.py, sous la condition ETUDIANT
        absences = Absence.objects.filter(etudiant=request.user)
        count = absences.count()
        return render(request, 'scolarite/accueil_etudiant.html', {'absences': absences, 'count': count})
    elif role == 'PROF':
        return render(request, 'scolarite/accueil_prof.html')
    else:
        return render(request, 'scolarite/accueil_admin.html')
    



def ajouter_absence(request):
    if request.user.profil.role.upper() != 'ADMIN' and not request.user.is_staff:
        return redirect('page_accueil')

    if request.method == 'POST':
        etudiant_id = request.POST.get('etudiant')
        matiere = request.POST.get('matiere')
        seance = request.POST.get('seance')
        
        # On crée l'objet en base de données
        Absence.objects.create(
            etudiant_id=etudiant_id,
            matiere=matiere,
            seance=seance
        )
        return redirect('page_accueil')

    etudiants = User.objects.filter(profil__role='ETUDIANT')
    return render(request, 'scolarite/admin_absences.html', {'etudiants': etudiants})


#absence solamente de l eleve connecte
@login_required
def liste_absences_etudiant(request):
    # On récupère les absences de l'étudiant connecté
    absences = Absence.objects.filter(etudiant=request.user).order_by('-date')
    count = absences.count()
    
    return render(request, 'scolarite/consultation_absences.html', {
        'absences': absences,
        'count': count
    })
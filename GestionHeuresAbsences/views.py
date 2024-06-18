from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('eleve/list')
        else:
            # Affiche un message d'erreur si les informations de connexion sont incorrectes
            error_message = "Nom d'utilisateur ou mot de passe incorrect"
            return render(request, 'GestionHeuresAbsences/pages/login.html', {'error_message': error_message})
    else:
        return render(request, 'GestionHeuresAbsences/pages/login.html')

# Eleves
def eleve_list(request):
    eleves = Eleve.objects.all()
    return render(request, 'GestionHeuresAbsences/pages/eleves/list.html', locals())

def eleve_create(request):
    form = EleveForm()
    if request.method == 'POST':
        form = EleveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('GestionHeuresAbsences:eleve_list')
    return render(request, 'GestionHeuresAbsences/pages/eleves/create.html', locals())

def eleve_update(request, id):
    instance = get_object_or_404(Eleve, id = id)
    form = EleveForm(instance = instance)
    if request.method == 'POST':
        form = EleveForm(request.POST, instance = instance)
        if form.is_valid():
            form.save()
            return redirect('GestionHeuresAbsences:eleve_list')
    return render(request, 'GestionHeuresAbsences/pages/eleves/update.html', locals())

def eleve_delete(request, id):
    instance = get_object_or_404(Eleve, id = id)
    instance.delete()
    return redirect('GestionHeuresAbsences:eleve_list')

# Absences
def absence_list_user(request, eleve_id):
    eleve = get_object_or_404(Eleve, id=eleve_id)
    absences = Absence.objects.filter(absences__id = eleve_id)
    return render(request, 'GestionHeuresAbsences/pages/absences/list_user.html', locals())

def absence_list(request):
    absences = Absence.objects.all()
    return render(request, 'GestionHeuresAbsences/pages/absences/list.html', locals())

def absence_create(request):
    form = AbsenceForm()
    if request.method == 'POST':
        form = AbsenceForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('GestionHeuresAbsences:absence_list')
    return render(request, 'GestionHeuresAbsences/pages/absences/create.html', locals())

def absence_update(request, id):
    instance = get_object_or_404(Absence, id = id)
    form = AbsenceForm(instance = instance)
    if request.method == 'POST':
        form = AbsenceForm(request.POST, instance = instance)
        if form.is_valid():
            form.save()
            return redirect('GestionHeuresAbsences:absence_list')
    return render(request, 'GestionHeuresAbsences/pages/absences/update.html', locals())

def absence_delete(request, id):
    instance = get_object_or_404(Absence, id = id)
    instance.delete()
    return redirect('GestionHeuresAbsences:absence_list')

# Justification
def justification_list_user(request, eleve_id):
    eleve = get_object_or_404(Eleve, id=eleve_id)
    justifications = Absence.objects.filter(absences__id = eleve_id)
    return render(request, 'GestionHeuresAbsences/pages/justifications/list_user.html', locals())

def justification_list(request):
    justifications = Justification.objects.all()
    return render(request, 'GestionHeuresAbsences/pages/justifications/list.html', locals())


def justification_create(request):
    form = JustificationForm()
    if request.method == 'POST':
        form = JustificationForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('GestionHeuresAbsences:justification_list')
    return render(request, 'GestionHeuresAbsences/pages/justifications/create.html', locals())

def justification_update(request, id):
    instance = get_object_or_404(Justification, id = id)
    form = JustificationForm(instance = instance)
    if request.method == 'POST':
        form = JustificationForm(request.POST, instance = instance)
        if form.is_valid():
            form.save()
            return redirect('GestionHeuresAbsences:justification_list')
    return render(request, 'GestionHeuresAbsences/pages/justifications/update.html', locals())

def justification_delete(request, id):
    instance = get_object_or_404(Justification, id = id)
    instance.delete()
    return redirect('GestionHeuresAbsences:justification_list')

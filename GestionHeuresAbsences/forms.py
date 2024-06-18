from django.forms import *
from .models import *

class EleveForm(ModelForm):
    class Meta:
        model = Eleve
        fields = ['matricule_E', 'nom_E', 'prenoms_E', 'sexe_E', 'classe']
        widgets = {
            'matricule_E': TextInput(attrs={
                'class': 'form-control form-control-sm form-element',
            }),

            'nom_E': TextInput(attrs={
                'class': 'form-control form-control-sm form-element',
            }),

            'prenoms_E': TextInput(attrs={
                'class': 'form-control form-control-sm form-element',
            }),

            'sexe_E': Select(attrs={
                'class': 'filter-option-inner-inner form-control',
            }),

            'classe': Select(attrs={
                'class': 'filter-option-inner-inner form-control',
            }),

        }


class AbsenceForm(ModelForm):
    class Meta:
        model = Absence
        fields = ['date_A', 'nombre_heures_A','eleve']
        widgets = {

            'date_A': DateInput(attrs={
                'class': 'form-control form-control-sm form-element',
            }),

            'nombre_heures_A': NumberInput(attrs={
                'class': 'form-control form-control-sm form-element',
            }),

            'eleve': Select(attrs={
                'class': 'filter-option-inner-inner form-control',
            }),
        }


class JustificationForm(ModelForm):
    class Meta:
        model = Justification
        fields = ['date_J', 'duree_J', 'Motifs','eleve']
        widgets = {

            'date_J': DateInput(attrs={
                'class': 'form-control form-control-sm form-element',
            }),

            'duree_J': NumberInput(attrs={
                'class': 'form-control form-control-sm form-element',
            }),

            'Motifs': Select(attrs={
                'class': 'filter-option-inner-inner form-control',
            }),

            'eleve': Select(attrs={
                'class': 'filter-option-inner-inner form-control',
            }),

        }
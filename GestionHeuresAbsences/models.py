from django.db import models

# Table Eleve
class Eleve(models.Model):
    CLASSES = [
        ('AS1A', 'AS1A'),
        ('AS1B', 'AS1B'),
        ('AS2A', 'AS2A'),
        ('AS2B', 'AS2B'),
        ('AS3', 'AS3'),
        ('ISE_eco', 'ISE_eco'),
        ('ISE_math', 'ISE_math'),
        ('ISE2A', 'ISE2A'),
        ('ISE2B', 'ISE2B'),
        ('ISE3', 'ISE3'),
    ]
    SEXE = [
        ('Masculin', 'Masculin'),
        ('Feminin', 'Feminin')
    ]

    matricule_E = models.CharField(max_length=50)
    nom_E = models.CharField(max_length=50)
    prenoms_E = models.CharField(max_length=75)
    sexe_E = models.CharField(max_length=10, choices=SEXE)
    classe = models.CharField(max_length=10, choices=CLASSES)


    class Meta:
        verbose_name = ("Eleve")
        verbose_name_plural = ("Eleves")

    def __str__(self):
        return self.matricule_E + '-' + self.nom_E


# Table Absences
class Absence(models.Model):
    date_A = models.DateField(null=True, blank=True)
    nombre_heures_A = models.IntegerField()
    eleve = models.ForeignKey('GestionHeuresAbsences.Eleve', verbose_name=("Eleve"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Absence")
        verbose_name_plural = ("Absences")

    def __int__(self):
        return str(self.date_A) + str(self.nombre_heures_A)


# Table Justifications
class Justification(models.Model):
    JUSTIFICATION = [
        ('CAS DE MALADIE', 'CAS DE MALADIE'),
        ('AUTORISATION ABSENCE', 'AUTORISATION ABSENCE'),
    ]

    date_J = models.DateField(null=True, blank=True)
    duree_J = models.IntegerField(null=True, blank=True)
    Motifs = models.CharField(max_length=50, choices=JUSTIFICATION)
    eleve = models.ForeignKey('GestionHeuresAbsences.Eleve', verbose_name=("Eleve"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Justification")
        verbose_name_plural = ("Justifications")

    def __str__(self):
        return self.Motifs
# Generated by Django 4.0.3 on 2022-03-04 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Absences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_Debut_Absences', models.DateField(blank=True, null=True)),
                ('date_Fin_Absences', models.DateField(blank=True, null=True)),
                ('nombre_heures_Absences', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Absences',
                'verbose_name_plural': 'Absence',
            },
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divisions_Classes', models.CharField(choices=[('Analyste Statisticien', 'Analyste Statisticien'), ('Adjoint Technique de la Statistique', 'Adjoint Technique de la Statistique'), ('Ingenieur des Travaux Statistiques', 'Ingenieur des Travaux Statistiques'), ('Ingenieur Statisticien Economiste', 'Ingenieur Statisticien Economiste')], max_length=50)),
                ('lib_Classes', models.CharField(choices=[('AS1', 'AS1'), ('AS2', 'AS2'), ('AD2', 'AD2'), ('ITS2', 'ITS2'), ('ISE_eco', 'ISE_eco'), ('ISE_math', 'ISE_math'), ('ISE2', 'ISE2'), ('ISE3', 'ISE3'), ('Master agricol', 'Master agricol')], max_length=50)),
            ],
            options={
                'verbose_name': 'Classes',
                'verbose_name_plural': 'Classe',
            },
        ),
        migrations.CreateModel(
            name='Eleves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule_E', models.CharField(max_length=50)),
                ('nom_E', models.CharField(max_length=50)),
                ('prenoms_E', models.CharField(max_length=75)),
                ('sexe_E', models.CharField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], max_length=10)),
                ('date_nais_E', models.DateField()),
                ('lieu_nais_E', models.CharField(max_length=50)),
                ('nationalite_E', models.CharField(choices=[('Ivoirienne', 'Ivoirienne'), ('Burkinabe', 'Burkinabe'), ('Malienne', 'Malienne'), ('Togolaise', 'Togolaise'), ('Guinéene', 'Guinéene'), ('Beninoise', 'Beninoise'), ('Senegalaise', 'Senegalaise'), ('Congolaise', 'Congolaise'), ('Gabonaise', 'Gabonaise'), ('Tchadienne', 'Tchadienne')], max_length=50)),
                ('email_E', models.EmailField(max_length=100)),
                ('situation_matrimoniale_E', models.CharField(choices=[('celibataire', 'Célibataire'), ('marie(e)', 'Marié(e)'), ('divorce(e)', 'Divorcé(e)'), ('veuf(veuve)', 'Veuf(veuve)')], max_length=50)),
                ('statut_professionnel_E', models.CharField(choices=[('Direct(e)', 'Direct(e)'), ('Professionnel(le)', 'Professionnel(le)')], max_length=50)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionHeuresAbsences.classes')),
            ],
            options={
                'verbose_name': 'Eleves',
                'verbose_name_plural': 'Eleve',
            },
        ),
        migrations.CreateModel(
            name='Semestres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lib_Semestres', models.CharField(choices=[('Semestre 1', 'Semestre 1'), ('Semestre 2', 'Semestre 2')], max_length=25)),
            ],
            options={
                'verbose_name': 'Semestres',
                'verbose_name_plural': 'Semestre',
            },
        ),
        migrations.CreateModel(
            name='Motifs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('justification_Motifs', models.CharField(choices=[('CAS DE MALADIE', 'CAS DE MALADIE'), ('AUTORISATION ABSENCE', 'AUTORISATION ABSENCE'), ('AUTRES', 'AUTRES')], max_length=50)),
                ('nombre_heures_Motifs', models.IntegerField()),
                ('date_Debut_motif', models.DateField(blank=True, null=True)),
                ('date_Fin_motif', models.DateField(blank=True, null=True)),
                ('absence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionHeuresAbsences.absences')),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionHeuresAbsences.eleves')),
            ],
            options={
                'verbose_name': 'Motifs',
                'verbose_name_plural': 'Motif',
            },
        ),
        migrations.AddField(
            model_name='absences',
            name='eleve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionHeuresAbsences.eleves'),
        ),
        migrations.AddField(
            model_name='absences',
            name='semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionHeuresAbsences.eleves'),
        ),
    ]

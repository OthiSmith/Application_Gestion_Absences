from django.urls import path
from . import views

app_name = 'GestionHeuresAbsences'

urlpatterns = [
    path('', views.login_view, name='login'),

    path('eleve/list', views.eleve_list, name='eleve_list'),
    path('eleve/create', views.eleve_create, name='eleve_create'),
    path('eleve/update/<int:id>', views.eleve_update, name='eleve_update'),
    path('eleve/delete/<int:id>', views.eleve_delete, name='eleve_delete'),

    path('absence_list', views.absence_list, name='absence_list'),
    path('absence/create', views.absence_create, name='absence_create'),
    path('absence/update/<int:id>', views.absence_update, name='absence_update'),
    path('absence/delete/<int:id>', views.absence_delete, name='absence_delete'),

    path('justification_list', views.justification_list, name='justification_list'),
    path('justification/create', views.justification_create, name='justification_create'),
    path('justification/update/<int:id>', views.justification_update, name='justification_update'),
    path('justification/delete/<int:id>', views.justification_delete, name='justification_delete'),
    ]
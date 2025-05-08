from django import forms

class CandidatForm(forms.Form):
    nom = forms.CharField(label="Nom", max_length=100)
    prenoms = forms.CharField(label="Prénoms", max_length=100)
    niveau_etude = forms.CharField(label="Niveau d'études", max_length=100)
    etablissement = forms.CharField(label="Établissement d'origine", max_length=150)
    concours = forms.CharField(label="Concours souhaité", max_length=100)
    extrait_naissance = forms.FileField(label="Extrait de naissance")
    certificat_nationalite = forms.FileField(label="Certificat de nationalité")
    lettre_motivation = forms.FileField(label="Lettre de motivation")
    diplome = forms.FileField(label="Diplôme")
    photo = forms.ImageField(label="Photo")
from django import forms
from .models import Candidat

class CandidatForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = '__all__'

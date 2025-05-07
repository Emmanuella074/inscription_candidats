from django.shortcuts import render
from .forms import CandidatForm  # ou le nom de ton formulaire

def accueil(request):
    return render(request, 'candidats/accueil.html')

def inscription_view(request):
    if request.method == 'POST':
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'candidats/success.html')  # page de succès optionnelle
    else:
        form = CandidatForm()
    return render(request, 'candidats/inscription.html', {'form': form})

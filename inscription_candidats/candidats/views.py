from django.shortcuts import render, redirect
from .forms import CandidatForm

def accueil(request):
    return render(request, 'candidats/accueil.html')

def inscription_view(request):
    if request.method == 'POST':
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('confirmation')  # nom de l'URL de confirmation
    else:
        form = CandidatForm()
    return render(request, 'candidats/inscription.html', {'form': form})

def confirmation(request):
    return render(request, 'candidats/confirmation.html')

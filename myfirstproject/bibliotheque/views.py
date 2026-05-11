from django.shortcuts import render
from .forms import LivreForm
from . import models

# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():
            Livre = form.save()
            return render(request, "bibliotheque/affiche.html", {"Livre" : Livre})
        else:
            return render(request,"bibliotheque/ajout.html", {"form" : form})
    else:
        form = LivreForm()
        return render(request,"bibliotheque/ajout.html", {"form" : form})

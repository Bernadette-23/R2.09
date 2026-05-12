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


def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save()
        return render(request,"bibliotheque/affiche.html", {"Livre": Livre})
    else:
        return render(request,"bibliotheque/ajout.html", {"form": lform})

def all(request):
    liste_livre = list(models.Livre.objects.all())
    return render(request, "bibliotheque/all.html", {"liste_livre": liste_livre})

def read(request, id):
    Livre = models.Livre.objects.get(pk=id)
    return render(request,"bibliotheque/affiche.html",{"Livre": Livre})

def update(request, id):
    livre = models.Livre.objects.get(pk=id)
    lform =

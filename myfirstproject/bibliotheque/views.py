from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LivreForm
from . import models
from .models import Livre

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
    lform = LivreForm(livre.__dict__)
    return render(request,'bibliotheque/update.html', {"livre":livre, "form":lform})
# ou  -->  lform = LivreForm(instace=livre)

#    all.html = update.html(dictionnaire)
#    return render(request, "bibliotheque/update.html", {"livvre": livre})

def updatetraitement(request, id):
    if request.method =="POST":
        lform = LivreForm(request.POST)
        if lform.is_valid():
            livre = lform.save(commit=False)
            livre.id = id
            livre.save()
            return HttpResponseRedirect("/bibliotheque/")
        else:
            livre = Livre.objects.get(pk=id)
            return render(request, 'bibliotheque/update.html', {"livre":livre, "form":lform})


def delete(request, id):
    livre = Livre.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect('/bibliotheque/')

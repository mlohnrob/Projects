from django.shortcuts import render
from .forms import *

# Create your views here.

def index(request):
    return render(request, "index.html")


def numberOfDrinks(request):
    if request.method =="POST":
        form = AlcForm(request.POST)
        if form.is_valid():
            volume = form.cleaned_data["V"]
            percent = form.cleaned_data["P"]

            drinks = volume*789*(percent/100)/12

            output = f"Genstande = {drinks}"
            return render(request, "numberOfDrinks.html", {"form": form, "output": output})

    form = AlcForm()
    return render(request, "numberOfDrinks.html", {"form": form})



def burningRate(request):
    if request.method == "POST":
        form = burningRateForm(request.POST)
        if form.is_valid():
            return render(request, "burningRate.html", {"form": form, "output": output})

    
    return render(request, "burningRate.html", {"form": form})

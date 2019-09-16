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
            output = ""
            return render(request, "burningRate.html", {"form": form, "output": output})


    return render(request, "burningRate.html", {"form": form})


def charmeIndex(request):
    if request.method == "POST":
        form = CharmeIndexForm(request.POST)
        if form.is_valid():
            sex = form.cleaned_data["sex"]
            drinks = form.cleaned_data["drinks"]
            mass = form.cleaned_data["mass"]
            hours = form.cleaned_data["hours"]
            minutes = form.cleaned_data["minutes"]

            if minutes == None:
                minutes = 0
            time = hours + minutes*(1/60)
            print(f"debug: {time}")

            Vi = drinks/time

            if sex == "male":
                permille = (Vi/mass-0.0083)*17.65*time
            elif sex == "female":
                permille = (Vi/mass-0.0083)*21.82*time


            if permille >= 0.3 and permille <= 0.6:
                output = f"Din promille er lig med: {permille}\nDu er vildt charmerende lige nu!"
            else:
                output = f"Din promille er lig med: {permille}"

            return render(request, "charmeIndex.html", {"form": form, "output": output})

    form = CharmeIndexForm()
    return render(request, "charmeIndex.html", {"form": form})

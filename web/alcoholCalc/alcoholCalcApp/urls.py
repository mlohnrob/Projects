from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("numberOfDrinks/", views.numberOfDrinks, name="numberOfDrinks"),
    path("burningRate/", views.burningRate, name="burningRate"),
    path("charmeIndex/", views.charmeIndex, name="charmeIndex"),
    path("createuser/", views.createUser, name="createUser"),
    path("login/", views.loginUser, name="login")
]

from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Client, Rent
from .forms import AddNewCar, AddNewClient, AddNewRent

# Create your views here.


def index(response):
    return render(response, "main/base.html", {})


def cars(response):
    cars = Car.objects.all()
    return render(response, "main/cars.html", {"cars": cars})


def clients(response):
    clients = Client.objects.all()
    return render(response, "main/clients.html", {"clients": clients})


def rents(response):
    rents = Rent.objects.all()
    return render(response, "main/rents.html", {"rents": rents})


def addCar(response):
    form = AddNewCar()
    return render(response, "main/add_car.html", {"form": form})


def addClient(response):
    form = AddNewClient()
    return render(response, "main/add_car.html", {"form": form})


def addRent(response):
    form = AddNewRent()
    return render(response, "main/add_car.html", {"form": form})
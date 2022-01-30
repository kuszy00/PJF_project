from django.shortcuts import render, redirect
from django.db.models import ProtectedError
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
    cars = Car.objects.all()
    return render(response, "main/rents.html", {"rents": rents, "cars": cars})


def addCar(response):
    form = AddNewCar()
    if response.method == 'POST':
        form = AddNewCar(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/cars')
    return render(response, "main/add_car.html", {"form": form})


def addClient(response):
    form = AddNewClient()
    if response.method == 'POST':
        form = AddNewClient(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/clients')
    return render(response, "main/add_client.html", {"form": form})


def addRent(response):
    form = AddNewRent()
    if response.method == 'POST':
        form = AddNewRent(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/rents')
    return render(response, "main/add_rent.html", {"form": form})


def updateCar(response, pk):
    update = Car.objects.get(id=pk)
    form = AddNewCar(instance=update)
    if response.method == 'POST':
        form = AddNewCar(response.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/cars')
    return render(response, "main/add_car.html", {"form": form})


def updateClient(response, pk):
    update = Client.objects.get(id=pk)
    form = AddNewClient(instance=update)
    if response.method == 'POST':
        form = AddNewClient(response.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/clients')
    return render(response, "main/add_client.html", {"form": form})


def updateRent(response, pk):
    update = Rent.objects.get(id=pk)
    form = AddNewRent(instance=update)
    if response.method == 'POST':
        form = AddNewRent(response.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/rents')
    return render(response, "main/add_rent.html", {"form": form})


def deleteCar(response, pk):
    delete = Car.objects.get(id=pk)
    if response.method == 'POST':
        try:
            delete.delete()
            return redirect('/cars')
        except ProtectedError:
            error = "delete"
            return render(response, "main/error.html", {"error": error})
    return render(response, "main/delete_car.html", {"item": delete})


def deleteClient(response, pk):
    delete = Client.objects.get(id=pk)
    if response.method == 'POST':
        try:
            delete.delete()
            return redirect('/clients')
        except ProtectedError:
            error = "delete"
            return render(response, "main/error.html", {"error": error})
    return render(response, "main/delete_client.html", {"item": delete})


def deleteRent(response, pk):
    delete = Rent.objects.get(id=pk)
    if response.method == 'POST':
        try:
            delete.delete()
            return redirect('/rents')
        except ProtectedError:
            error = "delete"
            return render(response, "main/error.html", {"error": error})
    return render(response, "main/delete_rent.html", {"item": delete})

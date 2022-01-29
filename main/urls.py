from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("cars/", views.cars, name="cars"),
    path("clients/", views.clients, name="clients"),
    path("rents/", views.rents, name="rents"),
    path("cars/add", views.addCar, name="add_car"),
    path("clients/add", views.addClient, name="add_client"),
    path("rents/add", views.addRent, name="add_rents")
]

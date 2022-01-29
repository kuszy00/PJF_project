from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("cars/", views.cars, name="cars"),
    path("clients/", views.clients, name="clients"),
    path("rents/", views.rents, name="rents"),
    path("cars/add/", views.addCar, name="add_car"),
    path("cars/update_car/<str:pk>/", views.updateCar, name="update_car"),
    path("cars/delete_car/<str:pk>/", views.deleteCar, name="delete_car"),
    path("clients/add/", views.addClient, name="add"),
    path("clients/update_client/<str:pk>/", views.updateClient, name="update_client"),
    path("clients/delete_client/<str:pk>/", views.deleteClient, name="delete_client"),
    path("rents/add/", views.addRent, name="add_rents"),
    path("rents/update_rent/<str:pk>/", views.updateRent, name="update_rent"),
    path("rents/delete_rent/<str:pk>/", views.deleteRent, name="delete_rent"),
]

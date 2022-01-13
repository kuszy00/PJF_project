from django.db import models


# Create your models here.
class Car(models.Model):
    plates = models.CharField('Numer rejestracyjny', max_length=8)
    manufacturer = models.CharField('Marka', max_length=30)
    model = models.CharField('Model', max_length=30)
    fuel = models.CharField('Rodzaj paliwa', max_length=10)
    mileage = models.IntegerField('Przebieg')
    vin = models.CharField('Numer VIN', max_length=17)
    price = models.IntegerField('Cena za 1 dzień')
    is_available = models.BooleanField('Dostępny', default=True)

    def __str__(self):
        return str(self.plates) + ' ' + str(self.manufacturer) + ' ' + str(self.model)


class Client(models.Model):
    name = models.CharField('Imie', max_length=20)
    surname = models.CharField('Nazwisko', max_length=20)
    mobile = models.CharField('Numer telefonu', max_length=12)
    address = models.CharField('Adres zamieszkania', max_length=100)

    def __str__(self):
        return str(self.name) + ' ' + str(self.surname) + ' nr: ' + str(self.mobile)


class Rent(models.Model):
    client = models.ForeignKey(Client)
    car = models.ForeignKey(Car)
    date = models.DateField('Data')
    days = models.IntegerField('Liczba dni')
    address = models.CharField('Miejsce wypożyczenia', max_length=100)

    def __str__(self):
        return str(self.date) + ' ' + str(self.car) + ' ' + str(self.client)

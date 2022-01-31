#Jakub Kowalski WCY19IJ3S1
import django_filters
from django_filters import *
from .models import *
from django.forms import DateInput


class CarFilter(django_filters.FilterSet):
    plates = CharFilter(lookup_expr='icontains', label='Numer rejestracyjny')
    manufacturer = CharFilter(lookup_expr='icontains', label='Marka')
    model =CharFilter(lookup_expr='icontains', label='Model')
    vin = CharFilter(lookup_expr='icontains', label='Numer VIN')

    class Meta:
        model = Car
        fields = ['is_available']


class ClientFilter(django_filters.FilterSet):
    name = CharFilter(lookup_expr='icontains', label='Imie')
    surname = CharFilter(lookup_expr='icontains', label='Nazwisko')
    mobile = CharFilter(lookup_expr='icontains', label='Numer telefonu')
    address = CharFilter(lookup_expr='icontains', label='Adres zamieszkania')


class RentFilter(django_filters.FilterSet):
    address = CharFilter(lookup_expr='icontains', label='Miejsce wypożyczenia')
    start_date = django_filters.DateFilter(field_name='date', lookup_expr='gte',
                                                   widget=DateInput(format='%Y-%m-%d"',
                                                                    attrs={'type': 'date'}), label="Data od")
    end_date = django_filters.DateFilter(field_name='date', lookup_expr='lte',
                                                   widget=DateInput(format='%Y-%m-%d"',
                                                                    attrs={'type': 'date'}), label="Data do")

    class Meta:
        model = Rent
        fields = ['client', 'car']
        labels = {
            'client': "Klient",
            'car': "Samochód"
        }
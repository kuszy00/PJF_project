from django.forms import ModelForm, widgets
from django import forms
from .models import Car, Client, Rent


class AddNewCar(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class AddNewClient(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class AddNewRent(ModelForm):
    car = forms.ModelChoiceField(queryset=Car.objects.filter(is_available=True))

    class Meta:
        model = Rent
        fields = ['client', 'car', 'date', 'days', 'address']
        labels = {
            'client': "Klient",
            'car': "Samochód"
        }
        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'})
        }


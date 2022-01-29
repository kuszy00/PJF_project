from django.forms import ModelForm
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


class DateInput(forms.DateInput):
    input_type = 'date'


class AddNewRent(forms.Form):
    client = forms.ModelChoiceField(label="Klient", queryset=Client.objects.all(), empty_label="")
    car = forms.ModelChoiceField(label="Samochód", queryset=Car.objects.all(), empty_label="")
    date = forms.DateField(label="Data", widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    days = forms.IntegerField(label="Liczba dni")
    address = forms.CharField(label="Miejsce wypożyczenia", max_length=100)
    widgets = {
        'date': DateInput(),
    }

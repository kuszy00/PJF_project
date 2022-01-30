#Jakub Kowalski WCY19IJ3S1
from datetime import timedelta, date
from main.models import Rent


# check availability
def changeAvailability():
    rents = Rent.objects.all()
    for item in rents:
        if item.car.is_available is False and item.date + timedelta(days=item.days) == date.today() - timedelta(days=1):
            Rent.is_rented(item)
            print("Availability updated")

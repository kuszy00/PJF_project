from django.contrib import admin
from .models import Car
from .models import Client
from .models import Rent

admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Rent)

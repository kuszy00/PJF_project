#Jakub Kowalski WCY19IJ3S1
from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    # scheduling checking availability
    def ready(self):
        from CarUpdate import updater
        updater.start()

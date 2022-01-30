#Jakub Kowalski WCY19IJ3S1
from apscheduler.schedulers.background import BackgroundScheduler
from .carUpdate import changeAvailability


# define schedule
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(changeAvailability, 'interval', minutes=60)
    scheduler.start()

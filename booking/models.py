from django.db import models
from transport.models import Vehicle
from location.models import Route
from parcel.models import Parcel

class Schedule(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()

class Booking(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

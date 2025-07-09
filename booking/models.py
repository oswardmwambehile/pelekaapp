from django.db import models
from transport.models import Vehicle
from location.models import Route
from parcel.models import Parcel
from django.conf import settings

class Schedule(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Schedule: {self.vehicle} on route {self.route} at {self.departure_time}"



class Booking(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)  # ✅ Use the import
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)    # ✅ Use the import
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Booking: {self.parcel} via {self.vehicle} on {self.date}"

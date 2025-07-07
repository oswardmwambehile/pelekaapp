from django.db import models
from booking.models import Booking  # Make sure this is correct

class TrackingStatus(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)  # e.g., In Transit, Delivered, etc.
    timestamp = models.DateTimeField(auto_now_add=True)
    gps_coordinates = models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        verbose_name_plural = "TrackingStatus"

    def __str__(self):
        return f"{self.booking} - {self.status} at {self.timestamp}"

from django.db import models
from booking.models import Booking

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='pending')  # 👈 Default value set here
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking} - {self.status} - {self.amount}"

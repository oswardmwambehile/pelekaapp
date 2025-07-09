from django.db import models
from account.models import CustomUser

# parcel/models.py

class Parcel(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    weight = models.FloatField()
    size = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='Pending')

    class Meta:
        unique_together = ('sender', 'name')

    def __str__(self):
        return self.name

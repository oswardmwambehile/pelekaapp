from django.db import models
from account.models import CustomUser

class TransportCompany(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    verified = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name


    class Meta:
        verbose_name_plural = "TransportCompanies"
    

class Vehicle(models.Model):
    company = models.ForeignKey(TransportCompany, on_delete=models.CASCADE)
    number_plate = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=50)
    capacity = models.FloatField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.company.company_name  
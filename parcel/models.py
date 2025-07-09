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

from rest_framework import serializers
from .models import Parcel

class ParcelSerializer(serializers.ModelSerializer):
    sender_email = serializers.EmailField(source='sender.email', read_only=True)
    sender_username = serializers.CharField(source='sender.username', read_only=True)
    sender_phone = serializers.CharField(source='sender.phone_number', read_only=True)
    sender_profile_picture = serializers.ImageField(source='sender.profile_picture', read_only=True)
    
    # ✅ Add this field to show the computed price
    price = serializers.SerializerMethodField()

    class Meta:
        model = Parcel
        fields = '__all__'  # includes all model fields + extra fields

    def get_price(self, obj):
        # Example pricing logic: base + per kg
        base_price = 3000
        rate_per_kg = 1000
        return base_price + (obj.weight * rate_per_kg)

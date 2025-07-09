from rest_framework import serializers
from .models import Parcel

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





class ParcelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = ['name', 'description', 'weight', 'size']  # example fields

    def validate_name(self, value):
        user = self.context['request'].user
        if Parcel.objects.filter(sender=user, name=value).exists():
            raise serializers.ValidationError("You already have a parcel with this name.")
        return value

    def create(self, validated_data):
        return Parcel.objects.create(**validated_data)

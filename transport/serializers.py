from rest_framework import serializers
from .models import TransportCompany,Vehicle

class TransportCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportCompany
        fields = ['id', 'company_name', 'description', 'verified']
        read_only_fields = ['id', 'verified']

    def validate(self, data):
        user = self.context['request'].user
        instance = getattr(self, 'instance', None)  # None if creating

        if not user.is_authenticated:
            raise serializers.ValidationError("Authentication required.")

        if user.user_type != 'transporter':
            raise serializers.ValidationError("Only transporters can create a transport company.")

        if instance is None:
            # Creation: check if user already has a company
            if TransportCompany.objects.filter(user=user).exists():
                raise serializers.ValidationError("You already have a transport company.")

        return data

    def create(self, validated_data):
        user = self.context['request'].user
        return TransportCompany.objects.create(user=user, **validated_data)





class VehicleSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)  # <- add this line

    class Meta:
        model = Vehicle
        fields = ['id', 'company', 'number_plate', 'vehicle_type', 'capacity', 'is_active']
        read_only_fields = ['id']

    def validate_number_plate(self, value):
        qs = Vehicle.objects.filter(number_plate__iexact=value)
        instance = getattr(self, 'instance', None)
        if instance:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This vehicle is already registered.")
        return value

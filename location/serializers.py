from rest_framework import serializers
from .models import Region, District

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'user']
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'region', 'user']
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)


from rest_framework import serializers
from .models import Route

class RouteSerializer(serializers.ModelSerializer):
    expected_time = serializers.DurationField()

    class Meta:
        model = Route
        fields = [
            'id',
            'origin',
            'destination',
            'distance',
            'expected_time',
            'user',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def create(self, validated_data):
        # Automatically assign the route to the currently authenticated user
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Prevent user change on update
        validated_data.pop('user', None)
        return super().update(instance, validated_data)



# Nested search serializer
from transport.models import  Vehicle, TransportCompany

class TransportCompanySearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportCompany
        fields = ['id', 'company_name', 'description', 'verified']

class VehicleSearchSerializer(serializers.ModelSerializer):
    company = TransportCompanySearchSerializer(read_only=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'number_plate', 'vehicle_type', 'capacity', 'is_active', 'company']

class RouteSearchSerializer(serializers.ModelSerializer):
    origin = serializers.StringRelatedField()
    destination = serializers.StringRelatedField()
    vehicles = VehicleSearchSerializer(many=True, read_only=True)

    class Meta:
        model = Route
        fields = ['id', 'origin', 'destination', 'distance', 'expected_time', 'vehicles']

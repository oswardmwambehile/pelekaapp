from rest_framework import serializers
from .models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    # Optional: show user info in response (read-only)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Schedule
        fields = ['id', 'vehicle', 'route', 'departure_time', 'user']
        read_only_fields = ['user']  # Prevent user from being passed via POST



from rest_framework import serializers
from transport.models import Vehicle
from parcel.models import Parcel
from .models import Booking

# Vehicle Serializer
class VehicleSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.company_name', read_only=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'number_plate', 'vehicle_type', 'capacity', 'is_active', 'company_name']

# Parcel Serializer with sender details
class ParcelSerializer(serializers.ModelSerializer):
    sender_email = serializers.EmailField(source='sender.email', read_only=True)
    sender_username = serializers.CharField(source='sender.username', read_only=True)
    sender_phone = serializers.CharField(source='sender.phone_number', read_only=True)
    sender_profile_picture = serializers.ImageField(source='sender.profile_picture', read_only=True)

    class Meta:
        model = Parcel
        fields = ['id', 'name', 'description', 'weight', 'size', 'status',
                  'sender_email', 'sender_username', 'sender_phone', 'sender_profile_picture']

# Booking Serializer nested with Vehicle and Parcel
class BookingSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)
    parcel = ParcelSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'vehicle', 'parcel', 'date', 'status']
        read_only_fields = ['date', 'status']

    def validate(self, attrs):
        user = self.context['request'].user
        parcel = attrs.get('parcel')

        if parcel.sender != user:
            raise serializers.ValidationError("You can only book your own parcels.")

        if Booking.objects.filter(parcel=parcel).exists():
            raise serializers.ValidationError("This parcel is already booked.")

        return attrs





class BookingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['status']

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Schedule
from .serializers import ScheduleSerializer

# Create
class ScheduleCreateAPIView(generics.CreateAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# List
class ScheduleListAPIView(generics.ListAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Schedule.objects.filter(user=self.request.user)

# Retrieve
class ScheduleDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Schedule.objects.filter(user=self.request.user)

# Update
class ScheduleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Schedule.objects.filter(user=self.request.user)

# Delete
class ScheduleDeleteAPIView(generics.DestroyAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Schedule.objects.filter(user=self.request.user)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def booking_create(request):
    serializer = BookingSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def booking_list(request):
    user = request.user
    bookings = Booking.objects.filter(parcel__sender=user).select_related('vehicle', 'parcel')
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer, BookingUpdateSerializer
from transport.models import Vehicle

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def company_bookings(request):
    """Transporter views bookings for all their vehicles."""
    user = request.user

    # Get vehicles owned by this user's company
    vehicles = Vehicle.objects.filter(company__user=user)
    bookings = Booking.objects.filter(vehicle__in=vehicles).select_related('vehicle', 'parcel')

    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_company_booking_status(request, booking_id):
    """Allow transporter to update booking status for their vehicles only."""
    user = request.user

    try:
        booking = Booking.objects.get(id=booking_id, vehicle__company__user=user)
    except Booking.DoesNotExist:
        return Response({"error": "Booking not found or not associated with your company."}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookingUpdateSerializer(booking, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

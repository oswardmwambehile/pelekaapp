from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from booking.models import Booking

# Create a payment manually
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def make_payment(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id, parcel__sender=request.user)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)

    data = request.data.copy()
    data['booking'] = booking.id

    serializer = PaymentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# List payments for the authenticated sender (user)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_payments(request):
    payments = Payment.objects.filter(booking__parcel__sender=request.user)
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data)


# Update payment status (optional, simulate verification)
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_payment_status(request, payment_id):
    try:
        payment = Payment.objects.get(id=payment_id, booking__parcel__sender=request.user)
    except Payment.DoesNotExist:
        return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)

    status_value = request.data.get('status')
    if status_value not in ['pending', 'success', 'failed']:
        return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)

    payment.status = status_value
    payment.save()
    return Response({'message': f'Payment marked as {status_value}'}, status=status.HTTP_200_OK)

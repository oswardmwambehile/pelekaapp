from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Parcel
from .serializers import ParcelSerializer, ParcelCreateSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_parcels(request):
    parcels = Parcel.objects.filter(sender=request.user)
    serializer = ParcelSerializer(parcels, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_parcel(request):
    many = isinstance(request.data, list)
    serializer = ParcelCreateSerializer(data=request.data, many=many, context={'request': request})
    if serializer.is_valid():
        # Pass sender only here, NOT in serializer.create()
        serializer.save(sender=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_parcel(request, pk):
    try:
        parcel = Parcel.objects.get(pk=pk, sender=request.user)
    except Parcel.DoesNotExist:
        return Response({'error': 'Parcel not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ParcelSerializer(parcel)
    return Response(serializer.data)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_parcel(request, pk):
    try:
        parcel = Parcel.objects.get(pk=pk, sender=request.user)
    except Parcel.DoesNotExist:
        return Response({'error': 'Parcel not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ParcelSerializer(parcel, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_parcel(request, pk):
    try:
        parcel = Parcel.objects.get(pk=pk, sender=request.user)
    except Parcel.DoesNotExist:
        return Response({'error': 'Parcel not found'}, status=status.HTTP_404_NOT_FOUND)

    parcel.delete()
    return Response({'message': 'Parcel deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

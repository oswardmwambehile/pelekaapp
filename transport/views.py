from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import TransportCompany, Vehicle
from .serializers import TransportCompanySerializer, VehicleSerializer
from .permissions import IsOwnerTransporter


class VehicleCreateView(generics.CreateAPIView):
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Optionally, you can enforce the company belongs to user (if needed)
        serializer.save()

class VehicleDetailView(generics.RetrieveAPIView):
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated, IsOwnerTransporter]

    def get_queryset(self):
        # Only vehicles from companies owned by the user
        return Vehicle.objects.filter(company__user=self.request.user)

class VehicleUpdateView(generics.UpdateAPIView):
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated, IsOwnerTransporter]

    def get_queryset(self):
        return Vehicle.objects.filter(company__user=self.request.user)

class VehicleDeleteView(generics.DestroyAPIView):
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated, IsOwnerTransporter]

    def get_queryset(self):
        return Vehicle.objects.filter(company__user=self.request.user)

class VehicleListView(generics.ListAPIView):
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # List vehicles only for companies owned by user
        return Vehicle.objects.filter(company__user=user)


class TransportCompanyCreateView(generics.CreateAPIView):
    serializer_class = TransportCompanySerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}

    def create(self, request, *args, **kwargs):
        user = request.user
        if TransportCompany.objects.filter(user=user).exists():
            return Response(
                {"detail": "You already have a transport company."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)


class TransportCompanyDetailView(generics.RetrieveAPIView):
    serializer_class = TransportCompanySerializer
    permission_classes = [IsAuthenticated, IsOwnerTransporter]

    def get_queryset(self):
        return TransportCompany.objects.filter(user=self.request.user)


class TransportCompanyUpdateView(generics.UpdateAPIView):
    serializer_class = TransportCompanySerializer
    permission_classes = [IsAuthenticated, IsOwnerTransporter]

    def get_queryset(self):
        return TransportCompany.objects.filter(user=self.request.user)


class TransportCompanyDeleteView(generics.DestroyAPIView):
    serializer_class = TransportCompanySerializer
    permission_classes = [IsAuthenticated, IsOwnerTransporter]

    def get_queryset(self):
        return TransportCompany.objects.filter(user=self.request.user)


class TransportCompanyListView(generics.ListAPIView):
    serializer_class = TransportCompanySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'transporter':
            return TransportCompany.objects.filter(user=user)
        return TransportCompany.objects.none()


